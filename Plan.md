 I want your help to create a claude command that will help me create new version, This is all the details about the process:
 1. When I am creating  a new version I generate new appcast and copy the new appcast to the repository,
 most of the time the name will be: appcast copy.xml or appcast 2.xml
 2. We should keep this file and not the source appcast.xml beacuse it have the new version details with hased signature
 3. Then I do this steps:
 Copy:
  <sparkle:fullReleaseNotesLink>
                https://appitstudio.github.io/extra-dock-updates/release-notes.html
            </sparkle:fullReleaseNotesLink>
    from the source appcast.xml to the new appcast copy.xml or appcast 2.xml
    Then add the description from the source appcast.xml to the new appcast copy.xml or appcast 2.xml
  <description><![CDATA[
  OLD DESCRIPTION
  ]]></description>

  Then I go to the release-notes.html file and add the new version notes at the top of the latest version for example:
  <div data-sparkle-version="3.9.1">
  </div>

  Then I tell LLM to write a release notes for the new version in a enthusiastic tone with emojis and user focused.

  Based on this inforamtion create a claude command that will help me create new version easily.
  The command will look up a file named: "version.md"
  The file will contain:
  VERSION: 3.9.1
DETAILS:
whats new in this version


ANd the command will use this information to create the new version notes and update the appcast file.
