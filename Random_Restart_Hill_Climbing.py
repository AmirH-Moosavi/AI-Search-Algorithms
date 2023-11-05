import time
import math
import numpy as np

# random hill climbing
def random_hillClimbing(step,start,end):

    startTime = time.time()
    x = (np.random.random() * (end-start))
    print('\nRandom-Restart Hill Climbing Search Algorithm with (step = %3.1f):'%step)
    localMax = False

    gStar = -1
    xStar = -1
    limit = 10000
    numIter = 0
    bound = 0.99
    Ascent = checkAscent(x,step)

    while numIter <= limit and gStar <= bound :
        if Ascent == True:
            numIter += 1
            g = math.sin(x)/x
            gNext = (math.sin(x + step))/(x + step)
            if g > gNext:
                if g > gStar:
                    xStar = x
                    gStar = g
                x = (np.random.random() * (end-start))
            else:
                x = x + step
        else:
            numIter += 1
            g = math.sin(x)/x
            gNext = (math.sin(x - step))/(x - step)
            if g > gNext:
                if g > gStar:
                    xStar = x
                    gStar = g
                x = (np.random.random() * (end-start))
            else:
                x = x - step            
    print('Number of iterations:', numIter)
    
    if gStar == -1:
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
random_hillClimbing(0.1,0.1,180)
random_hillClimbing(1,0.1,180)