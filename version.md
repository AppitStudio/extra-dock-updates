VERSION: 4.1.2
DETAILS:
Multi-Monitor Support Improvements

  - Enhanced dock positioning on multiple monitors - Completely refactored dock position handling to ensure docks stay where you placed them when reopening the app. Docks no longer unexpectedly shift across displays.
  - New screen resolution strategy - Implemented smarter screen identification with improved fallback strategies when monitor configurations change.
  - Post-launch position validation - Added DockPositionValidationService that validates and corrects dock positions after app launch, ensuring accurate restoration based on your preferences.
  - Deferred dock visibility - Docks now wait until position validation completes before appearing, eliminating visual jumps during app launch.

  Fullscreen App Compatibility

  - Fixed screen switching issue - Interacting with the dock while using fullscreen apps no longer causes unexpected space/screen switches. The dock window no longer becomes key or main, maintaining your current workspace.

  Auto-Hide Enhancements

  - Edge-sensitive reveal - Auto-hidden docks now respond when your mouse approaches screen edges, making the feature more intuitive for docks fixed to left or right positions.
  - Smoother animations - Configurable show/hide animation durations provide smoother transitions when the dock appears and disappears.
  - Backup mouse tracking - Added a polling mechanism that ensures consistent mouse tracking behavior even when the dock is hidden, improving overall responsiveness.

  Widget Improvements

  - Live configuration updates - Widget settings now apply immediately without requiring multiple selections or re-opening the configuration panel.
  - LiveDock widget sizing - The LiveDock widget now automatically recalculates dock size when visible items change, with proper positioning adjustments.

  General Improvements

  - Enhanced collapse/expand settings for better user experience
  - Improved dock state persistence and restoration logic

  ---
