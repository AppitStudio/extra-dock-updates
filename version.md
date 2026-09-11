VERSION: 4.3.16
DETAILS:

new: Smooth native-style icon magnification - icons swell as the pointer moves along the dock and settle back as it leaves; Live Dock and Space Awareness apps magnify too, other widgets and controls slide aside; on by default at 1.5x with Maximum size and Falloff radius controls in Dock Properties
new: Live Clock and Calendar icons - a Clock item shows the current time (refreshed every second) and a Calendar item shows today's date (flips at local midnight); a custom icon still takes precedence
new: Drag handle placement setting per dock - Automatic, Screen edge, Inward, Left/Top or Right/Bottom
improved: Sharper icons at every size - icons keep vector/IconServices representations and are rendered at full hover size so magnification never enlarges base-size pixels
improved: Notification badges are attached to the icon artwork and follow hover magnification, drop-target enlargement and the launch bounce
improved: Hovering across a Live Dock no longer re-scans every running app or rebuilds context menus on every pointer move
bug fix: Docks, item labels and hover previews stay on screen through Hide Others and Cmd+H
bug fix: Widgets inside a Notch layout dock follow the notch surface color and stay readable in Light appearance
