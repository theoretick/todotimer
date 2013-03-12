#!/usr/bin/env python
##################################################
# name: todotimer.py
# auth: lucas c
# url: http://github.com/theoretick
# desc: v1.1 simple pomodoro-style configurable todo timer
##################################################
# - reads todo.txt
# - per line from infile, assigns session time for task
# - asks(?) user for timelength, or checks a config(?)
# - notifies start
# - notifies break
# - rinse, repeat
# - FUTURE - keep logs
# - FUTURE - tag support
# - FUTURE - parse filename for matching date (ex todo2mar2012.txt)
# - FUTURE - pull todo from XXXXX?? cool!
#       i.e. iCloud, evernote, dropbox, etc.
##################################################
# fix:
# - no break at end of session
# - better format break, bold "up next?"
# - consider: wait and then call notify instantly?
# - should break/task be separate functions?
##################################################


from lib import timer

if __name__=="__main__":
    try:
        infile = open('todo.txt','r')
        inputline = infile.readline()
    except:
        raise InputError, "Error, no todo.txt found"
        exit()
    while inputline:
        timer.timer(inputline, 'task')
        inputline = infile.readline()
        if inputline:
            timer.timer(inputline, 'break')
    infile.close()
    timer.timer('Done!','end')