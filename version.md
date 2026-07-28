VERSION: 4.3.3
DETAILS:

new: Copy or move items between docks — right-click any dock item or widget in the Management window and use the new "Copy to Dock ▸" / "Move to Dock ▸" menus to send it to another preset or to all docks at once; widget rows now also have a full context menu (Configure, Duplicate, Copy, Move, Remove)
new: GPU Usage widget — a fourth System Stats gauge alongside CPU, Memory, and Battery that reads live GPU utilization from IOKit on both Apple Silicon and Intel Macs; says so instead of showing a misleading 0% when no GPU reports a figure
new: Text color for System Stats widgets — CPU, GPU, RAM, and Battery gauges gain an Automatic / White / Black / custom Text Color setting covering the number, metric label, and battery percentage; Automatic stays the default
new: Clock — Show Day of Week — the Clock's Custom layout can now show short weekday names on their own ("Mon") or combined with the date ("Mon, Oct 23"); included in the Full preset
bug fix: Empty Trash now works with Full Disk Access — a denied delete reported by macOS as a write-permission error is now recognized as a permission problem, so the Finder fallback engages, verifies the trash is actually empty afterwards, and the alert distinguishes a genuine permission denial from an unrelated failure
bug fix: Respect Dock Space on every screen — with "Show dock on all screens" enabled, each per-screen dock now reserves its own space so app windows no longer expand underneath the dock on other displays
bug fix: Clock seconds no longer hidden on small docks — "Show Seconds" (and the date and timezone) are honored on docks under 40px; visibility is now driven purely by your settings
bug fix: Timer widget settings apply instantly — editing a timer's duration, label, accent color, or font size now takes effect immediately instead of waiting for the widget to be recreated
improved: Replaced deprecated APIs (kIOMasterPortDefault, NSOpenPanel.allowedFileTypes, icon(forFileType:)), cleared assorted compiler warnings, and added new test coverage for trash error classification, GPU utilization parsing, Timer configuration sync, and clock layout options
