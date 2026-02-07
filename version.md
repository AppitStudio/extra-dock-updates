VERSION: 4.1.3
DETAILS:
REMOVE TECHNICAL DETAILS AND KEEP ONLY THE USER FOCUSED DETAILS
# ExtraDock V4.1.3 Release Notes

**Release Date:** February 7, 2026

---

## New Features

### Desktop Widget Mode
- New per-dock "Act as Desktop Widget" toggle in dock properties
- When enabled, the dock sits behind app windows like embedded desktop content
- Smart interaction: dock temporarily elevates to the front on click, drag, or right-click, then automatically demotes back after 1.25 seconds of inactivity
- Desktop widget docks auto-hide when a fullscreen app is detected on their screen
- Persisted in V5 dock data with full backward-compatible Codable support

### Hide Native macOS Dock
- New global setting in General Settings: "Hide native macOS Dock"
- Suppresses Apple's Dock by applying a deep autohide delay (1000s) via `defaults write`
- Snapshots your current Dock preferences before hiding, restores them exactly when toggled off
- Automatically re-applied on app launch if the setting is enabled

---

## Bug Fixes

### Safari Web App / Alias URL Resolution
- Fixed adding Safari web apps and alias/symlink items to docks
- Both drag-and-drop and the Add Item dialog now resolve aliases, symlinks, and bookmark-style URLs before checking file existence
- Added fallback application search across `~/Applications`, `/Applications`, and `/System/Applications` when the raw URL doesn't point to an existing file
- Refactored duplicated item-creation logic into shared `resolveItemURL()`, `makeDockItem()`, and `isApplicationBundle()` helpers in both `DragAndDropHandler` and `DockItemsTab`
- Duplicate detection now uses the resolved path instead of the raw dropped URL

### V5 DockBehavior Codable Compatibility
- Added explicit `init(from:)` decoder and `encode(to:)` encoder for `DockBehavior`
- The new `desktopWidget` field decodes gracefully as `nil` from older saved data, preventing crashes on upgrade

### Swift 6 Actor Isolation Fix
- Fixed actor isolation warning in desktop widget fullscreen detection by wrapping the screen check in a `Task { @MainActor in }` block

---

## Internal Improvements

- `DragAndDropHandler`: Eliminated duplicated item-building code between drag-and-drop and add-dialog paths
- `DockItemsTab`: Consolidated URL resolution and item building into reusable private methods
- `CustomWindow`: Centralized window level and collection behavior assignment through `updateWindowLevelForMode()`
- Removed stale `collectionBehavior` assignment in screen-move code path
- Updated SearchBar SPM package pin
