# ExtraDock Updates - Copilot Instructions

## Project Overview
This repository manages the Sparkle auto-update feed for ExtraDock, a macOS dock management application by AppIt Studio. The primary purpose is to distribute app updates and release notes through Sparkle's RSS-based update system.

## Key Files & Architecture

### Core Update Files
- **`appcast.xml`** - Production Sparkle update feed (RSS format)
  - Contains single `<item>` element with latest version info
  - **Critical fields:** `sparkle:version` (build number), `sparkle:shortVersionString` (display version), `enclosure url` (DMG download), `sparkle:edSignature` (security signature)
  - Links to hosted `release-notes.html` via `sparkle:fullReleaseNotesLink`
- **`release-notes.html`** - Styled release notes displayed in Sparkle updater
  - Uses `data-sparkle-version` attributes for version-specific styling
  - Current version marked with `.sparkle-installed-version` CSS class
- **`appcast-example.xml`** - Template/reference for different app (DockFlow)

### Release Notes Structure
- Modern Apple-style CSS with system fonts and rounded cards
- Each version in separate `<div data-sparkle-version="X.Y">` container
- Semantic HTML with proper heading hierarchy (h2 for version, h3 for sections)
- Emojis used for visual appeal in headings

## Update Workflow
1. **Version Bump:** Update version numbers in `appcast.xml`
   - Increment `sparkle:version` (build number)
   - Update `sparkle:shortVersionString` (semantic version)
   - Update `pubDate` to current timestamp
2. **Release Notes:** Add new version section at top of `release-notes.html`
3. **DMG & Signature:** Update `enclosure url` and `sparkle:edSignature` when new build available
4. **Commit:** Single commit with format like "bump v3.9" or "V3.8"

## Sparkle Integration Details
- **Update URL:** Points to GitHub Pages hosting (`https://appitstudio.github.io/extra-dock-updates/appcast.xml`)
- **EdDSA Signatures:** Uses `sparkle:edSignature` for secure update verification
- **Minimum System:** Currently requires macOS 11.5+
- **File Hosting:** DMG files hosted on GitHub Releases (`/releases/download/prod/extraDock.dmg`)

## Content Patterns
- **Version Format:** Major.Minor.Patch (e.g., "3.9.1")
- **Feature Categories:** "What's New & Improved", "Technical Improvements", "Bug Fixes"
- **Marketing Tone:** Enthusiastic with emojis, emphasizes user benefits and community
- **Historical Context:** References company acquisition (AppIt Studio acquiring from previous owner)

## Development Notes
- Repository uses GitHub Pages for hosting static files
- No build process required - direct XML/HTML editing
- Version control follows simple linear history
- `.vscode/settings.json` disables Nuxt detection (not a Nuxt project)

## Common Tasks
- **New Release:** Copy latest `<item>` in appcast.xml, update version fields, add corresponding section to release-notes.html
- **Hotfix:** Follow same process but increment patch version only
- **Historical Reference:** Check git log for version bump patterns and release note formatting examples
