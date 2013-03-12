#!/usr/bin/env python
##################################################
# name: todotimer.py
# auth: lucas c
# url: http://github.com/theoretick
# desc: simple pomodoro-style configurable todo timer
##################################################
# - reads todo.txt
# - per line from infile, assigns session time for task
# - asks(?) user for timelength, or checks a config(?)
# - notifies start
# - notifies break
# - rinse, repeat
# - FUTURE - keep logs
# - FUTURE - tag support
# - FUTURE - parse filename for matching date (ex todo2mar2012.txt)
# - FUTURE - pull todo from XXXXX?? cool!
#		i.e. iCloud, evernote, dropbox, etc.
##################################################
# fix:
# - no break at end of session
# - better format break, bold "up next?"
# - consider: wait and then call notify instantly?
# - should break/task be separate functions?
##################################################

########## config vars
TASKLENGTH = 25
BREAKLENGTH = 5

def timer(taskname, timeslot='break'):
        """
        takes taskname and timeslot category as args.
        
        """


        from lib import pyNotificationCenter
        import time

	########## init variables
	title = taskname
	tasktext = "Starting {} min counter".format(TASKLENGTH)
        endtext = """
               Congrats, you're done for today"""
	breaktext = """
	       Finished session, take a {} minute break.\n
	       Up next: {}"
	       """.format(BREAKLENGTH, taskname)
	tasktime = TASKLENGTH * 60
	breaktime = BREAKLENGTH * 60

	# run notification loops based on timeslot (task, end, or break)

	if timeslot == 'task':
		pyNotificationCenter.notify(title, tasktext)
                time.sleep(tasktime)
        elif timeslot== 'end':
                pyNotificationCenter.notify(title, endtext)
	else:
		pyNotificationCenter.notify('Rest!', breaktext)
                time.sleep(breaktime)
        return True

if __name__=="__main__":
	try:
		infile = open('todo.txt','r')
	        inputline = infile.readline()
	except:
		raise InputError, "Error, no todo.txt found"
		exit()
	while inputline:
		timer(inputline, 'task')
		inputline = infile.readline()
		if inputline:
                    timer(inputline, 'break')
	infile.close()
        timer('Done!','end')
