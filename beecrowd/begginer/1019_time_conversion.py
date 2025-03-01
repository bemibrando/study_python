"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.
"""

def convertTime(value):
    hours = value // 3600
    rest = value % 3600
    minutes = rest // 60
    seconds  = rest % 60
    print("%d:%d:%d" %(hours, minutes, seconds))
    
secondsInput = int(input())
convertTime(secondsInput)