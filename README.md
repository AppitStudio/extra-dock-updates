# ExtraDock V4 updates

`appcast.xml` is the append-only Sparkle feed for the `v4-stable` Keyper release track. New releases are prepended; published items and their release metadata are never removed or rewritten because `pubDate` is the update-entitlement enforcement signal.

The retained history begins at 4.1.2. Those versions have immutable, version-tagged GitHub Release assets. The already-published 4.3.7 item is preserved byte-for-byte from the production feed; reconstructed 4.1.2–4.3.5 items use independently verifiable GitHub publish timestamps. Older feed revisions referenced the moving `prod` asset, and some had inconsistent or backdated dates, so they remain visible in Git history but are not safe enforcement records.

## Release workflow

1. Prepend the newly signed item to `appcast.xml` with its immutable `vX.Y.Z` release URL and real publish date. Never backdate a release.
2. Run `python3 scripts/validate_appcast.py appcast.xml`.
3. Open a pull request. CI compares the feed with the base revision and rejects removed or mutated release metadata.
4. After merge, GitHub Pages must expose the new first item before CI registers every retained release with Keyper. Registration is idempotent.

Repository administrators must configure one Actions secret named `KEYPER_RELEASE_TOKEN`. It is the dedicated server-only credential issued for ExtraDock's `v4-stable` release track. Never use the validation API key embedded in the app.
