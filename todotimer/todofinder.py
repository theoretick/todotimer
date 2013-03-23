# -*- coding: utf-8 -*-
#
# Part of todotimer.py
# locates todo.txt, called from todotimer.py
#

def todofinder():
    """ locates todo.txt file
     - if DROPBOX is on, attempts to find file there
     - else, defaults to local directory
    """
    from todotimer.config import DROPBOX
    from todotimer.config import FILENAME
    from os import path

    HOME = path.expanduser('~')
    DROPBOXPATH = HOME+'/Dropbox/'+FILENAME

    if path.exists(DROPBOXPATH) & (DROPBOX == True):
    	print "Accessing ", DROPBOXPATH
        return DROPBOXPATH
    else:
    	print "Using current directory todo.txt"
        return FILENAME