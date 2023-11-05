import math
import time
import numpy as np
# Hill-Climbing
def hillClimbing(step,start,end):
    startTime = time.time()

    x = (np.random.random() * (end-start))
    print('\nHill-Climbing Search Algorithm with (step = %3.1f):'%step)
    localMax = False
    gStar = -10
    xStar = -10
    Ascent = checkAscent(x,step)

    while localMax == False and x <= end:
        if Ascent == True:
            g = math.sin(x)/x
            gNext = (math.sin(x + step))/(x + step)
            if g > gNext:
                xStar = x
                gStar = g
                localMax = True
            else:
                x = x + step
        else:
            g = math.sin(x)/x
            gNext = (math.sin(x - step))/(x - step)
            if g > gNext:
                xStar = x
                gStar = g
                localMax = True
            else:
                x = x - step            
    if gStar == -10:
        print('There is no local maximum with this x random number')
    else:
        Error = 1 - gStar
        endTime = time.time()
        tRun = endTime - startTime
        print('x*:', xStar)
        print('g(x*):', gStar)
        print('time: ', tRun)
        print('Error: ', Error)

def checkAscent(x,step):
    if math.sin(x)/x > math.sin(x - step)/(x - step):
        return(True)
    else:
        return(False) 
    
    
hillClimbing(0.1,0,180)
hillClimbing(1,0,180)