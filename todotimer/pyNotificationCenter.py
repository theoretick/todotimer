# -*- coding: utf-8 -*-
# Python integration with Mountain Lion's notification center
# original code forked from maranas at
# https://github.com/maranas
#
# Part of todotimer.py

import Foundation, objc

NSUserNotification = objc.lookUpClass('NSUserNotification')
NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')

def notify(title, info_text, delay=0, sound=True, userInfo={}):
    """ Python method to show a desktop notification on Mountain Lion.
        - Delay in seconds
        - userInfo: a dictionary that can be used to handle clicks in your
                    app's applicationDidFinishLaunching:aNotification method
    """
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setInformativeText_(info_text)
    notification.setUserInfo_(userInfo)
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)
