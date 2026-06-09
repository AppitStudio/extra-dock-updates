VERSION: 4.2.8
DETAILS:

new: Show on All Screens — per-dock toggle that mirrors one dock onto every connected display, auto-managing as screens connect/disconnect
new: Desktop Widget Mode — per-dock setting that keeps the dock on the desktop, behind app windows
new: Space Awareness widget — right-click a window to act on it directly
new: Automatic Backups section in Settings — view, refresh, reveal in Finder, and restore previous configuration backups
new: Accessibility permission reminder prompting users to grant access required for window focus/switching
improved: More reliable monitor identity — docks reappear on the correct screen after unplug/replug/rearrange
improved: Refreshed screen settings UI for assigning docks to specific monitors
improved: Live Dock no longer shows apps twice when they are also pinned manually
improved: Live Dock refreshing is lower-overhead with a lifecycle fix to stay in sync as apps launch/quit
improved: Snappier dock-icon clicks — faster activation and window detection
improved: Smarter Respect Dock Space handling for newly opened windows
improved: Reduced background CPU usage (lower-frequency mouse polling, throttled badge reads, deduplicated window tracking)
improved: Smoother, more reliable onboarding first-run experience
improved: Larger custom spacers — size limit raised to 3000
improved: Full backup export/import improvements, including fixed export save defaults
bug fix: Dock click "half-focus" bug on macOS 14 & 15 — clicking an icon now brings the window front, not just the menu bar
bug fix: Cross-Space and multi-monitor windows (including Electron/Chromium apps like Claude, Chrome, VS Code) now reliably raised on click
bug fix: Auto-hide reliability — prevents a dock from incorrectly hiding when it should stay visible
