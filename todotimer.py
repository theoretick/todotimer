#!/usr/bin/env python
##################################################
# name: todotimer.py
# auth: lucas c
# url: http://github.com/theoretick
# desc: v2.0 simple pomodoro-style configurable todo timer
##################################################
# - reads in-folder todo.txt
# - assigns session time to each line (task) from infile
# - notifies task start and break
# - rinse, repeat
##################################################

from todotimer.timer import timer
from todotimer.todofinder import todofinder

if __name__=="__main__":
    try:
        infile = open(todofinder())
        inputline = infile.readline()
    except:
        raise IOError, "Error, no todo.txt found"
        exit()

    while inputline:
        timer(inputline, 'task')
        inputline = infile.readline()
        if inputline:
            timer(inputline, 'break')
    infile.close()
    timer('DONE!','end')
