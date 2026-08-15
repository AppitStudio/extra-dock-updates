VERSION: 4.3.5
DETAILS:

bug fix: Microsoft Teams no longer quits and relaunches when clicked in a dock — new Microsoft Teams (com.microsoft.teams2) is a multi-process WebView2 app whose process group can't survive ExtraDock's window-raise sequence (Accessibility writes + private window-server calls), so clicking it could make the whole group cleanly quit and relaunch ~15–20 seconds later, losing session state; Teams is now activated exclusively through the public NSWorkspace/LaunchServices activation path the native Dock uses, and other affected apps can be quirked without an update via the ExtraDockPublicActivationOnlyBundleIDs defaults array (trade-off for quirked apps: dock clicks focus the app as a whole, so per-window cycling and minimize-toggle from the dock are unavailable)
