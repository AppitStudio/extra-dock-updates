VERSION: 4.1.7
DETAILS:
ExtraDock — What's New

ExtraDock Release Notes

  App Window Previews (Beta)

  The headline feature of this release. Hover over any running app icon in your ExtraDock to see live window
  previews - Optional in the settings

  Preview Features:
  - Live window thumbnail previews on icon hover with real-time screen captures
  - Window action buttons (close, minimize, maximize) directly from the preview panel
  - Click a preview thumbnail to activate that specific window
  - Smart filtering of ghost/utility windows so only real windows are shown
  - Support for minimized and hidden windows (configurable)
  - Current-space-only filtering option
  - Multiple sort orders: most recent, alphabetical, creation time, or screen position
  - Background preview cache service for faster hover response

  Preview Customization (Settings > App Previews):
  - Preview panel size and thumbnail quality
  - Window title visibility (on hover or always)
  - Sort order and filtering options (hidden windows, minimized windows, current space only)
  - Control button position (multiple layout options)
  - Compact mode with configurable title format and item size
  - Window capture quality (nominal vs best)

  Permissions:
  - Requires Screen Recording permission (opt-in, off by default)
  - macOS Tahoe (26+) compatibility with extra permission validation

  Improved Click Behavior

  - Normal click on a running app now activates the app instead of relaunching it

  Bug Fixes

  - Collapse/Expand positioning fix: Collapse button no longer drifts after toggling on macOS Tahoe. The resize now
  uses a button-anchor approach that preserves the collapse button's screen position through expand/collapse
  transitions
  - Tahoe collapse timing: Increased animation settle delay from 50ms to 400ms to prevent capturing mid-animation
  frames
  - CustomWindow frame management: New syncFrameToCollapseState() method bypasses anchor-preservation logic during
  collapse state transitions, fixing cases where the window would jump to incorrect positions
  - Hidden dock fix: Fixed issue where dock could become hidden/invisible
