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
from todotimer.config import FILEPATH

if __name__=="__main__":
    try:
        infile = open(FILEPATH)
        inputline = infile.readline()
    except:
        raise InputError, "Error, no todo.txt found"
        exit()

    while inputline:
        timer(inputline, 'task')
        inputline = infile.readline()
        if inputline:
            timer(inputline, 'break')
    infile.close()
    timer('DONE!','end')
