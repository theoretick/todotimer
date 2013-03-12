# -*- coding: utf-8 -*-
#
# timer for tasks and breaks called from todotimer.py
#

def timer(taskname, timeslot='break'):
    """ timer function for tasks & breaks
        - takes taskname and timeslot category as args
        - uses timeslot to determine notification call
        - calls pyNotificationCenter for notifications
    """
    from todotimer import pyNotificationCenter
    from todotimer.config import TASKLENGTH
    from todotimer.config import BREAKLENGTH
    import time

    ########## init variables
    tasktext = "Starting {} min counter".format(TASKLENGTH)
    endtext = """
        Congrats, you're done for today"""
    breaktext = """
        Finished session, take a {} minute break.\n
        Up next: {}"
        """.format(BREAKLENGTH, taskname)
    tasktime = TASKLENGTH #* 60
    breaktime = BREAKLENGTH #* 60
    ########## run notification loops based on timeslot (task, end, or break)
    if timeslot == 'task':
        pyNotificationCenter.notify(taskname, tasktext)
        time.sleep(tasktime)
    elif timeslot== 'end':
            pyNotificationCenter.notify(taskname, endtext)
    else:
        pyNotificationCenter.notify('Rest!', breaktext)
        time.sleep(breaktime)