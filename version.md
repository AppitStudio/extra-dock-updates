VERSION: 4.1.8
DETAILS:
Improved: High-Resolution App Icons — Dock icons are now rendered at 128pt logical size instead of 32pt, resulting in crisp, sharp icons on Retina displays. Also fixes the macOS Tahoe issue where icons
  appeared padded inside a square container.

  Added: Invisible Dock Mode — Setting background opacity to 0 now produces a truly invisible dock with no lingering borders, gradients, shadows, or outlines. Icons float cleanly on the desktop.

  Bug Fix: Notification Badges Crash on Multi-Monitor Setups — Fixed a crash caused by a force-cast in the Accessibility API when reading window positions on multi-monitor configurations.

  Bug Fix: Notification Badges Deadlock — Replaced a blocking main-thread dispatch with a thread-safe lock, preventing potential app freezes when reading badge counts.

  Bug Fix: Live Dock Notification Badges — Notification badges now work independently on Live Dock and Space Awareness widgets. Previously, badges only appeared if the app was also added to a regular
  ExtraDock.

  Added: System Settings Badge — ExtraDock now detects pending macOS software updates and shows a red badge dot on the System Settings icon, matching native Dock behavior.

  Added: App Launch Bounce Animation — Launching an app from the dock now triggers a macOS-style bounce animation, giving visual feedback that the app is opening.

  Added: URL Widget Duplicate Button — Quickly duplicate URL widgets to reuse styling. The duplicate copies colors and icon settings but clears the URL, opening the config sheet for the new link.

  Improved: URL Widget Identification — URL widgets now show their domain name in the management list instead of "Utility Widget", making it easy to tell them apart.

  UX: Context Menu Cleanup — Removed app names from context menu buttons (just "Open" instead of "Open Chrome"). Reordered to match macOS Dock: Open > Reveal in Finder > Hide > Quit. Consistent across all
   locations (dock items, Live Dock, Space Awareness).

  UX: Collapse Button — 3-Character Limit — Text/emoji collapse buttons now support up to 3 characters with auto-sizing, up from 1.

  UX: Accent Color Picker Always Visible — The dock accent/tint color picker is now visible even when collapse mode is set to None, since it also affects the dock edge tint.

  UX: Effects & Collapse Sections Expanded by Default — The Effects and Collapse Button settings sections now open expanded instead of collapsed.

  Improved: Notification Badge Text — Badge numbers now use medium weight instead of bold for a cleaner look.

  Added: Shelf Widget — Completed shelf widget with drag-and-drop support, floating panel, and visual improvements.

  Improved: Drag-and-Drop — Better drag-and-drop into floating windows with dashed-line visual indicators for clarity.
