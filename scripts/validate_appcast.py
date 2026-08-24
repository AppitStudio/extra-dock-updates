#!/usr/bin/env python3
"""Validate ExtraDock's production appcast and enforce append-only metadata."""

from __future__ import annotations

import argparse
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

SPARKLE = "http://www.andymatuschak.org/xml-namespaces/sparkle"
NS = {"sparkle": SPARKLE}
SIGNATURE = f"{{{SPARKLE}}}edSignature"


@dataclass(frozen=True)
class Release:
    version: str
    build: str
    published_at: datetime
    minimum_system_version: str
    url: str
    length: str
    signature: str


def required_text(item: ET.Element, path: str, label: str) -> str:
    value = item.findtext(path, namespaces=NS)
    if value is None or not value.strip():
        raise ValueError(f"missing {label}")
    return value.strip()


def parse_appcast(xml: bytes, source: str) -> list[Release]:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as error:
        raise ValueError(f"{source}: invalid XML: {error}") from error

    releases: list[Release] = []
    for index, item in enumerate(root.findall("./channel/item"), start=1):
        try:
            version = required_text(item, "sparkle:shortVersionString", "short version")
            build = required_text(item, "sparkle:version", "build version")
            pub_date = required_text(item, "pubDate", "pubDate")
            minimum = required_text(item, "sparkle:minimumSystemVersion", "minimum system version")
            enclosure = item.find("enclosure")
            if enclosure is None:
                raise ValueError("missing enclosure")
            url = enclosure.attrib["url"].strip()
            length = enclosure.attrib["length"].strip()
            signature = enclosure.attrib[SIGNATURE].strip()
            published_at = parsedate_to_datetime(pub_date)
            if published_at.tzinfo is None:
                raise ValueError("pubDate must include a timezone")
        except (KeyError, ValueError) as error:
            raise ValueError(f"{source}: item {index}: {error}") from error

        if not build.isdecimal() or int(build) <= 0:
            raise ValueError(f"{source}: {version}: build must be a positive integer")
        if not length.isdecimal() or int(length) <= 0:
            raise ValueError(f"{source}: {version}: enclosure length must be positive")
        expected_url = (
            "https://github.com/AppitStudio/extra-dock-updates/releases/download/"
            f"v{version}/extraDock.dmg"
        )
        if url != expected_url:
            raise ValueError(f"{source}: {version}: enclosure must use its immutable v{version} release")
        if len(signature) < 80:
            raise ValueError(f"{source}: {version}: missing or truncated EdDSA signature")

        releases.append(Release(version, build, published_at, minimum, url, length, signature))

    if not releases:
        raise ValueError(f"{source}: feed has no releases")

    versions = [release.version for release in releases]
    builds = [release.build for release in releases]
    if len(versions) != len(set(versions)):
        raise ValueError(f"{source}: duplicate short versions")
    if len(builds) != len(set(builds)):
        raise ValueError(f"{source}: duplicate build versions")
    if releases != sorted(releases, key=lambda release: release.published_at, reverse=True):
        raise ValueError(f"{source}: items must be newest-first by pubDate")
    if releases != sorted(releases, key=lambda release: int(release.build), reverse=True):
        raise ValueError(f"{source}: items must be newest-first by build")

    return releases


def baseline_xml(git_ref: str, path: Path) -> bytes | None:
    if not git_ref or set(git_ref) == {"0"}:
        return None
    result = subprocess.run(
        ["git", "show", f"{git_ref}:{path.as_posix()}"],
        check=False,
        capture_output=True,
    )
    return result.stdout if result.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("appcast", type=Path)
    parser.add_argument("--baseline-git-ref", default="")
    args = parser.parse_args()

    try:
        current = parse_appcast(args.appcast.read_bytes(), str(args.appcast))
        previous_xml = baseline_xml(args.baseline_git_ref, args.appcast)
        if previous_xml is not None:
            previous = parse_appcast(previous_xml, f"{args.baseline_git_ref}:{args.appcast}")
            current_by_version = {release.version: release for release in current}
            for release in previous:
                if current_by_version.get(release.version) != release:
                    raise ValueError(
                        f"append-only violation: release {release.version} was removed or its metadata changed"
                    )
    except (OSError, ValueError) as error:
        print(f"appcast validation failed: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(current)} append-only ExtraDock releases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
