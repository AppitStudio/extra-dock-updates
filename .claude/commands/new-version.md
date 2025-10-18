You are helping to publish a new version of ExtraDock. Follow these steps carefully:

## Step 1: Read version.md
Read the `version.md` file to get:
- VERSION: The version number (e.g., 3.9.1)
- DETAILS: What's new in this version

## Step 2: Find the new appcast file
Look for a file named either:
- `appcast copy.xml`
- `appcast 2.xml`

This file is generated from the build process and contains the new version with the hashed signature.

## Step 3: Extract content from current appcast.xml
From the current `appcast.xml`, extract:
1. The `<sparkle:fullReleaseNotesLink>` section (including the full element)
2. The `<description>` section (including the full CDATA content)
3. The `enclosure url` value from the `<enclosure>` tag

## Step 4: Update the new appcast file
Add the extracted content to the new appcast file:
1. Add the `<sparkle:fullReleaseNotesLink>` section after `<sparkle:minimumSystemVersion>`
2. Add the `<description>` section after the `</sparkle:fullReleaseNotesLink>` closing tag
3. Update the `url` attribute in the `<enclosure>` tag to use the correct GitHub releases URL from the source appcast.xml (https://github.com/AppitStudio/extra-dock-updates/releases/download/prod/extraDock.dmg instead of the appitstudio.github.io URL)

## Step 5: Generate release notes
Using the DETAILS from version.md, generate enthusiastic release notes following this format:
- Main title: `ExtraDock {VERSION} – [Creative Subtitle]! [Emoji]`
- Section headings with emojis (e.g., "✨ What's New & Improved", "🔧 Technical Improvements", "🚀 What's Next?")
- Use bullet points with `<strong>Feature Name:</strong> description` format
- Write in an enthusiastic, user-focused tone
- Include emojis in headings
- End with a thank you message to the ExtraDock community

## Step 6: Update the new appcast file's description
Replace the `<description>` content in the new appcast file with the newly generated release notes, wrapped in proper CDATA format:
```xml
<description><![CDATA[
[Generated release notes HTML here]
]]></description>
```

## Step 7: Update release-notes.html
Add a new `<div data-sparkle-version="{VERSION}">` section at the top of the `<body>` tag (right after `<body>`), containing the same release notes HTML.

## Step 8: Replace appcast.xml
Replace the current `appcast.xml` with the updated new appcast file content.

## Step 9: Clean up
Delete the temporary appcast file (appcast copy.xml or appcast 2.xml).

## Important Notes:
- Maintain the exact XML structure and formatting
- Preserve all CDATA sections properly
- Ensure the EdDSA signature from the new appcast file is preserved
- Follow the existing release notes style and structure
- Be enthusiastic and user-focused in your tone
