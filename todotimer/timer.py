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
    from todotimer import config
    from time import sleep

    ########## init variables
    # Parse task from project or context
    title, project, context = tags(taskname)
    if not context:
        context = ''
    if not project:
        project = ''

    ########## main
    tasktext = """
        {} {}
        Starting {} min counter
        """.format(project, context, config.TASKLENGTH)
    endtext = """
        Congrats, you're done for today"""
    breaktext = """
        Finished session, take a {} minute break.\n
        Next: {}
        """.format(config.BREAKLENGTH, taskname)
    tasktime = config.TASKLENGTH #* 60
    breaktime = config.BREAKLENGTH #* 60

    ########## run notification loops based on timeslot (task, end, or break)
    if timeslot == 'task':
        pyNotificationCenter.notify(title, tasktext, 0, config.SOUND)
        sleep(tasktime)
    elif timeslot== 'end':
        pyNotificationCenter.notify(taskname, endtext, 0, config.SOUND)
    else:
        pyNotificationCenter.notify('Rest!', breaktext, 0, config.SOUND)
        sleep(breaktime)
