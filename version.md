VERSION: 4.1.9
DETAILS:
Hello ExtraDockers 👋🏻,



🖥️ Attach to Screen → Attach to Screen(s)

Seems like a small change right?! Wrong!

Attach to Screen was one of those obvious features ExtraDock needed… If I connect at my Ultra wide screen → show this dock.

The issue? Well, there were 5 main bug reports with it, but 2 stood out.





If I have two workstations like Home and Office, I can’t attach to both, only one works and the other breaks it. Annoying.



Identical monitors… Same problem as someone else’s identical twins… ExtraDock just couldn’t tell them apart… (sorry parents with identical twins)





The solution? Rework that thing from the ground up, make it recognize screens by a unique ID on the hardware info, and finally, allow multiple attachments.

This ties directly to the “Docks don’t save position/screen attachment after restart/sleep” bug that we’ve been dealing with, and after closing the lid of my Mac about a 100 times (it helped catching bugs by the way) and restarting my Mac 6 times (WHILE ACTIVELY DEVELOPING 💀) — there’s improvement. I don’t think it’s perfect yet, I’ll need your feedback and bug reports to make it completely consistent (please, and thank you 😘).

📣 I need your help!

I said so in previous newsletters, there are times to develop, and there are times to perfect. Now’s the time to perfect.

Usually during big development phases with lots of changes in both UI and backend, we prefer to ship updates faster, in order to get user’s feedback and improve based on that feedback.

Now, after massive development in the last couple of months, we’re going to fix some stuff, and for that, we need to know what’s broken for you.

Screen assignments is the first wave of fixes to an annoying problem.

If you got any more problems, or you feel like something is unclear or needs some attention — drop us an email. We absolutely want to fix stuff, but we can’t know what’s not working for you if you don’t tell us 😄



🪵 Change log:

⚡improvement: Docks can now be assigned to multiple monitors.
⚡improvement: ExtraDock now recognizes monitor that have docks attached to them by utilizing hardware information every screen exposes to the OS.
⚡improvement: All screens you connect to are automatically register, you can choose to Forget screens you don’t want to see. 

💠 attention: macOS likes to add “Phantom Screens”, as I discover more cases where users suddenly see a random screen called “Primary Screen (1920×1080)” in their dropdown, I’ll find ways to block it. This is a bug that doesn’t affect you at all, out of 8 beta testers, only 2 had this issue (that I am aware of).

🐞 bug fix: Fixed an issue where dock settings could get mixed up between docks when restoring connection.
🐞 bug fix: Fixed a race condition bug that caused issues with auto-hide on full-width docks.
🐞 bug fix: Fixed a bug where dragging docks that are attached to screen would cause the other screen to “adopt” that dock, and make it attached to itself (clingy much?)

📋 user interface: Attach to Screen has been changed to Screen Assignment. You will find a dropdown menu showing all your known monitors with indicators whether they are connected (green) disconnected (white), and a V sign that indicates if the dock should appear when that screen is connected.
