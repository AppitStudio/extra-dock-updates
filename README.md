ExtraDock Updates

# ExtraDock V4 beta registration

The V4 `beta` GitHub pre-release is distributed without an appcast entry.
Publishing it triggers `register-keyper-releases.yml`, which registers the
release title's version (for example `B4.4.0` → `4.4.0`) with Keyper as a
prerelease. This lets installed beta builds pass license version checks while
the stable update target remains the latest stable appcast version. The mutable
`beta` download URL is deliberately omitted from Keyper's release history.

The release must contain `extraDock.dmg`, and the workflow requires the existing
`KEYPER_RELEASE_TOKEN` secret for the V4 stable track.
