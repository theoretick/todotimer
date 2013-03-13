# -*- coding: utf-8 -*-
#
# Functions for added tag support
# 

def tags(inline):
    """ 
      If TAGSUPPORT on, return tag
      else, return False
    """
    from todotimer.config import TAGSUPPORT

    if TAGSUPPORT == False:
        return False

    if '@' in inline:
        linelist = inline.split('@')
        tag = linelist([len(linelist)-1]
        return tag
