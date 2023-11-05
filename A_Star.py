import time
import math
def AStar(ep, br, m):
    startTime = time.time()

    print('\n***A* Algorithm with epsilon %5.2f, branching factor %d and depth limit %d:***' %(ep,br,m))
    depth = 0
    goal = 0
    valid_range = [0.1,180]
    
    while (depth != m and goal != 1):
        temp = []
        depth += 1
        devided = (valid_range[1] - valid_range[0]) / br
        first = valid_range[0]
        print('\nDepth: ', depth)
        for i in range(0,br):
            temp.append([first, (first + devided)])
            first = temp[-1][-1]
        position, goal, xStar,gStar = check_succerssors_AStar(temp, ep, depth)
        valid_range = temp[position]
        print('Valid range: ' , valid_range)
        
    Error = abs((1 - gStar)/1)
    if goal == 0:
        print('Global Maximum does not found.')
    else:
        print('Answer was it the %d th depth', depth)
    endTime = time.time()
    tRun = endTime - startTime
    print()
    print('x*:', xStar)
    print('g(x*):', gStar)
    print('time: ', tRun)
    print('Error: ', Error)

def check_succerssors_AStar(temp, ep, g):
    ytemp = []
    xList = []
    goal = 0
    for ranges in temp:
        x = (ranges[0] + ranges[1]) /2
        xList.append(x)
        y = abs(math.sin(x)/x)
        f = y + g
        if y >= ep:
            goal = 1
            print('The goal is:' , y)
        ytemp.append(f)
    gStar = (max(ytemp)-g)
    yIndex = ytemp.index(max(ytemp))
    print('Maximum Y: ', gStar)
    return(yIndex, goal, xList[yIndex], gStar)

AStar(0.9, 2, 40)