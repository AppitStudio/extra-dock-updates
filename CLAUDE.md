# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository manages the Sparkle auto-update feed for ExtraDock, a macOS dock management application by AppIt Studio. The repository's sole purpose is to distribute app updates and release notes through Sparkle's RSS-based update system via GitHub Pages.

## Architecture

### Core Files
- **`appcast.xml`** - Production Sparkle update feed in RSS format
  - Contains a single `<item>` element with the latest version information
  - Critical fields: `sparkle:version` (build number), `sparkle:shortVersionString` (display version), `enclosure url` (DMG download link), `sparkle:edSignature` (EdDSA security signature)
  - Links to `release-notes.html` via `sparkle:fullReleaseNotesLink`
  - Hosted URL: `https://appitstudio.github.io/extra-dock-updates/appcast.xml`

- **`release-notes.html`** - Styled HTML page displayed in the Sparkle updater window
  - Each version is wrapped in a `<div data-sparkle-version="X.Y.Z">` container
  - CSS automatically marks current version with `.sparkle-installed-version` class
  - Uses Apple-style design with system fonts and rounded cards
  - New versions are added at the top, older versions below

- **`appcast-example.xml`** - Reference template from a different app (DockFlow), kept for structural reference

### Sparkle Integration
- **Minimum System Version:** macOS 11.5+
- **Security:** Uses EdDSA signatures (`sparkle:edSignature`) for secure update verification
- **File Hosting:** DMG files hosted on GitHub Releases at `/releases/download/prod/extraDock.dmg`
- **Distribution:** GitHub Pages serves the static XML/HTML files

## Common Development Tasks

### Publishing a New Release

When publishing a new version of ExtraDock:

1. **Update `appcast.xml`:**
   - Increment `sparkle:version` (integer build number, e.g., 390 → 391)
   - Update `sparkle:shortVersionString` (semantic version, e.g., "3.9" → "3.9.1")
   - Update `pubDate` to current timestamp in RFC 2822 format
   - Update `enclosure url` if DMG location changes
   - Update `sparkle:edSignature` with the new EdDSA signature from the build process
   - Update the inline `<description>` CDATA section with release notes (formatted HTML)

2. **Update `release-notes.html`:**
   - Add a new `<div data-sparkle-version="X.Y.Z">` section at the top (after `<body>` tag)
   - Structure: h2 for main version title, h3 for category headings, ul/li for features
   - Categories typically include: "What's New & Improved", "Technical Improvements", "Bug Fixes"
   - Use emojis in headings for visual appeal (following existing pattern)
   - Keep content user-focused and enthusiastic in tone

3. **Commit:**
   - Use simple commit messages following repository patterns: "bump v3.9", "V3.8", "version bump"
   - Single commit per version bump

### Version Numbering
- Format: `Major.Minor.Patch` (e.g., "3.9.1")
- Build numbers are sequential integers (e.g., 391, 392, etc.)
- Note: Project moved from v1.x versioning to v3.x format (mentioned in v3.9.1 notes)

### Content & Tone Guidelines
- Use enthusiastic, user-focused language
- Emphasize user benefits over technical implementation details
- Include emojis in release note headings
- Reference the AppIt Studio community and thank users
- Maintain semantic HTML structure with proper heading hierarchy

## Technical Notes

- **No build process:** This is a static file repository - direct XML/HTML editing only
- **GitHub Pages:** Repository is configured to serve files via GitHub Pages
- **No programming languages:** Pure XML/HTML/CSS content management
- **Linear history:** Version bumps follow a simple sequential commit pattern
- **Validation:** Sparkle framework handles XML validation when the app checks for updates

## Historical Context

ExtraDock was acquired by AppIt Studio (creators of DockFlow) and has been maintained under new ownership since version 3.4. Release notes often reference this transition and the commitment to ongoing development.
