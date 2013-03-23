## Todo Timer ##

A simple pomodoro-style todo timer that pulls items from todo.txt

At start/end of session pushes notifications to OSX's Notification Center.

### Usage ###

Run timer.py in folder containing _"todo.txt"_. Program pulls items line-by-line
at time intervals specified (default 25min with 5min breaks) in config file.

Formatting is dead simple. Example todo file:  
>  read dhalgren +chapteraday @home  
>  watch stargate  
>  review anki @computer  
>  work on resume +findajob  

Tag format matches [todo.txt app](http://todotxt.com) style:
 - @ marks context (where you need to be to do X)
 - + marks project (what project X belongs to)

**Tags must go at END of line**

### Todo ###

 - Add logging for future analysis
 - Add parsing for daily todos (i.e. todo2mar2013.txt) and date matching
 - Add scanning of common todo folders (i.e. Dropbox)
	- Add iCloud support...?
 - Integrate with todo.txt project
