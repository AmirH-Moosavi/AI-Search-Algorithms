import math
import time
# Comlplete-Search Algorithm
def complete_Search(step,start,end):
    startTime = time.time()

    x = start
    xStar = -1
    gStar = -1
    gStarTrue = 1

    while x <= end:
        x = x + step
        g = math.sin(x)/x
        if g >= gStar:
            gStar = g
            xStar = x

    Error = abs((gStarTrue - gStar)/gStarTrue)
    endTime = time.time()
    tRun = endTime - startTime

    print('\nComplete Search with (step = %3.1f):' %step)
    print('x*:', xStar)
    print('g(x*):', gStar)
    print('time: ', tRun)
    print('Error: ', Error)
    
complete_Search(0.1,0,180)
complete_Search(1,0,180)