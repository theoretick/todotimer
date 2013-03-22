# -*- coding: utf-8 -*-
#
# Part of todotimer.py
# Function for added tag support
# 

def tags(inline):
    """ Adds Tagsupport for both Context and Project
     If CONTEXT on, split and return title with tag
     If PROJECT on, split and return title with tag

    """
    from todotimer.config import CONTEXT
    from todotimer.config import PROJECT

    if (CONTEXT == True) & ('@' in inline):
        linelist = inline.split('@')
        taskname = linelist[0]
        contexttag = linelist[1]
        projecttag = False
        if (PROJECT == True) & ('+' in taskname):
            linelist = taskname.split('+')
            taskname = linelist[0]
            projecttag = linelist[1]
        print taskname, projecttag, contexttag
        return taskname, projecttag, contexttag
    else:
        return inline, False, False