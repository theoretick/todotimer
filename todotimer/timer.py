# -*- coding: utf-8 -*-
#
# Part of todotimer.py
# timer for tasks and breaks called from todotimer.py
#

def timer(taskname, timeslot='break'):
    """ timer function for tasks & breaks
        - uses timeslot to determine notification call
        - notifies via pyNotificationCenter
    """
    from todotimer import pyNotificationCenter
    from todotimer.tags import tags
    from todotimer.config import TASKLENGTH
    from todotimer.config import BREAKLENGTH
    from todotimer.config import SOUND
    import time

    ########## init variables
    title, project, context = tags(taskname)
    if not context:
        context = ''
    if not project:
        project = ''

    ##########
    tasktext = """
        {} {}
        Starting {} min counter
        """.format(project, context, TASKLENGTH)
    endtext = """
        Congrats, you're done for today"""
    breaktext = """
        Finished session, take a {} minute break.\n
        Next: {}
        """.format(BREAKLENGTH, taskname)
    tasktime = TASKLENGTH * 60
    breaktime = BREAKLENGTH * 60

    ########## run notification loops based on timeslot (task, end, or break)
    if timeslot == 'task':
        pyNotificationCenter.notify(title, tasktext, 0, SOUND)
        time.sleep(tasktime)
    elif timeslot== 'end':
            pyNotificationCenter.notify(taskname, endtext, 0, SOUND)
    else:
        pyNotificationCenter.notify('Rest!', breaktext, 0, SOUND)
        time.sleep(breaktime)
