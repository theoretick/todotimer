# -*- coding: utf-8 -*-
#
# Part of todotimer.py
# locates todo.txt, called from todotimer.py
# for now, just searches dropbox for todo folder

def todofinder():
    """ locates todo.txt file.
     - if DROPBOX is on, attempts to find file there
     - else, defaults to local directory
    """
    from todotimer.config import DROPBOX
    from todotimer.config import FILENAME
    from os import path

    HOME = path.expanduser('~')
    DROPBOXPATH = HOME+'/Dropbox/todo/'+FILENAME
    LOCATION = FILENAME
    ACCESSMSG = "Using current dir '{}'".format(FILENAME)

    if DROPBOX == True:
        if path.exists(DROPBOXPATH):
            	ACCESSMSG = "Accessing {}".format(DROPBOXPATH)
                LOCATION = DROPBOXPATH
        else:
            ACCESSMSG = """Dropbox path: '{}' not found.\n{}
                """.format(DROPBOXPATH, ACCESSMSG)

    print ACCESSMSG
    return LOCATION