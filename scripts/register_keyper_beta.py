#!/usr/bin/env python3
"""Register the published, mutable ExtraDock V4 beta with Keyper."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime


DEFAULT_ENDPOINT = "https://keyper.appitstudio.com/api/releases"
VERSION_RE = re.compile(r"B(4\.\d+\.\d+)$")


def beta_payload(event: dict) -> dict[str, object]:
    release = event["release"]
    if event["repository"]["full_name"] != "AppitStudio/extra-dock-updates":
        raise ValueError("Unexpected release repository")
    if release["tag_name"] != "beta" or release["prerelease"] is not True:
        raise ValueError("Expected the published ExtraDock V4 beta release")
    match = VERSION_RE.fullmatch(release["name"])
    if match is None:
        raise ValueError("Beta release title must be B followed by a V4 version")
    if not any(asset.get("name") == "extraDock.dmg" for asset in release["assets"]):
        raise ValueError("Published beta release has no extraDock.dmg asset")
    published_at = release["published_at"]
    if not isinstance(published_at, str) or datetime.fromisoformat(
        published_at.replace("Z", "+00:00")
    ).tzinfo is None:
        raise ValueError("Published beta release has no timestamp with timezone")

    # The beta tag is replaced on every upload. Keep its mutable download URL
    # out of the immutable Keyper history while allowing version checks.
    return {
        "version": match.group(1),
        "released_at": published_at,
        "is_prerelease": True,
    }


def register(endpoint: str, token: str, payload: dict[str, object]) -> int:
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "appit-updates-release-sync/1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"Keyper rejected beta with HTTP {error.code}: {body}") from error


def main() -> int:
    try:
        event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
        payload = beta_payload(event)
        token = os.environ.get("KEYPER_RELEASE_TOKEN", "").strip()
        if not token:
            raise ValueError("KEYPER_RELEASE_TOKEN is required")
        endpoint = os.environ.get("KEYPER_RELEASE_ENDPOINT", "").strip() or DEFAULT_ENDPOINT
        if not endpoint.startswith("https://"):
            raise ValueError("KEYPER_RELEASE_ENDPOINT must use HTTPS")
        status = register(endpoint, token, payload)
        print(f"Registered ExtraDock V4 beta {payload['version']} (HTTP {status})")
    except (KeyError, OSError, ValueError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
