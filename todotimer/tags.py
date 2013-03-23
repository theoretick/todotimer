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

    if (CONTEXT == True) or (PROJECT == True):
        linelist = inline.split()        
        if '@' in linelist[-1]:
            contexttag = linelist.pop(-1)
        elif '@' in linelist[-2]:
            contexttag = linelist.pop(-2)
        else:
            contexttag = False

        if '+' in linelist[-1]:
            projecttag = linelist.pop(-1)
        elif '+' in linelist[-2]:
            projecttag = linelist.pop(-2)
        else:
            projecttag = False
        return " ".join(linelist[:]), projecttag, contexttag

    return inline, False, False