#!/usr/bin/env python3
"""Idempotently register every retained appcast release with Keyper."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

SPARKLE = {"sparkle": "http://www.andymatuschak.org/xml-namespaces/sparkle"}


def releases(xml: bytes) -> list[tuple[str, str]]:
    root = ET.fromstring(xml)
    result: list[tuple[str, str]] = []
    for item in root.findall("./channel/item"):
        version = item.findtext("sparkle:shortVersionString", namespaces=SPARKLE)
        pub_date = item.findtext("pubDate")
        if version is None or pub_date is None:
            raise ValueError("validated appcast unexpectedly lacks release metadata")
        released_at = parsedate_to_datetime(pub_date).astimezone(timezone.utc).isoformat()
        result.append((version.strip(), released_at))
    return result


def wait_until_published(feed_url: str, expected_version: str, attempts: int = 30) -> None:
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(feed_url, timeout=15) as response:
                remote = releases(response.read())
            if remote and remote[0][0] == expected_version:
                return
        except (OSError, ET.ParseError, ValueError):
            pass
        if attempt + 1 < attempts:
            time.sleep(10)
    raise RuntimeError(f"published feed did not reach version {expected_version}")


def register(endpoint: str, token: str, version: str, released_at: str) -> None:
    body = json.dumps({"version": version, "released_at": released_at}).encode()
    request = urllib.request.Request(
        endpoint,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "extra-dock-updates-release-registry/1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status not in (200, 201):
                raise RuntimeError(f"Keyper returned HTTP {response.status}")
    except urllib.error.HTTPError as error:
        detail = error.read(512).decode(errors="replace")
        raise RuntimeError(f"Keyper returned HTTP {error.code}: {detail}") from error


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("appcast", type=Path)
    parser.add_argument("--endpoint", default="https://keyper.appitstudio.com/api/releases")
    parser.add_argument("--feed-url")
    args = parser.parse_args()

    token = os.environ.get("KEYPER_RELEASE_TOKEN", "").strip()
    if not token:
        print("KEYPER_RELEASE_TOKEN is required", file=sys.stderr)
        return 1

    try:
        retained = releases(args.appcast.read_bytes())
        if args.feed_url:
            wait_until_published(args.feed_url, retained[0][0])
        for version, released_at in reversed(retained):
            register(args.endpoint, token, version, released_at)
            print(f"Registered ExtraDock {version}")
    except (OSError, RuntimeError, ValueError, ET.ParseError) as error:
        print(f"release registration failed: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
