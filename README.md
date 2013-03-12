## Todo Timer ##

A simple pomodoro-style todo timer, defaults set to 25 min sessions with
5 min breaks. Pulls items from todo.txt.  At start/end of session pushes
notification to OSX's Notification Center.

### Usage ###

Run timer.py in folder containing todo.txt. Program pulls items line-by-line
at task time interval specified (default 25min with 5min breaks) in init variables.

### Todo ###

 - Add tag support
 - Add logging for future analysis
 - Add parsing for daily todos (i.e. todo2mar2013.txt) and date matching
 - Add scanning of common todo folders (i.e. Dropbox)
	- Add iCloud support...?

