# -*- coding: utf-8 -*-
#
# part of todotimer.py
# config settings for todotimer
####################

# todo.txt default name and filepath
FILENAME = 'todo.txt'

# specify the length of a task session (default 25)
TASKLENGTH = 15

# specify the length of a break (default 5)
BREAKLENGTH = 10

# audio on/off (default True)
SOUND = True

####################
# Advanced features
####################

# Support for TAGS in todo lists (i.e. @home or @work, +cleanhouse or +findjob)
# - context or project MUST be last on line (order of each not important)
CONTEXT = True
PROJECT = True

# Support for logging of previous todo lists
# CURRENTLY NOT IMPLEMENTED
LOGGING = False

# enable Dropbox support for todo.txt storage
DROPBOX = False
