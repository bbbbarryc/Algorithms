#!/usr/bin/env python
# "Custom" logging script
import time
import random

startTime = 0.0
endTime = 0.0

def logStart():
    global startTime
    startTime = time.time()

def logEnd():
    global startTime, endTime
    endTime = time.time()
    print "Time: " + str(endTime - startTime)
    
