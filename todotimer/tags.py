# -*- coding: utf-8 -*-
#
# Part of todotimer.py
# Function for added tag support
# 

def tags(inline):
    """ If TAGSUPPORT on, split and return title with tag
    """
    from todotimer.config import TAGSUPPORT

    if (TAGSUPPORT == True) & ('@' in inline):
        linelist = inline.split('@')
        taskname = linelist[0]
        tasktag = linelist[1]
        return taskname, tasktag
    else:
        return inline, False