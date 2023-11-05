import time

def GBFS(ep, br, m):
    startTime = time.time()
    print('\n***GBFS Algorithm with Epsilon %5.2f, Branching factor %d and Depth limit %d:***' %(ep,br,m))
    depth = 0
    goal = 0
    valid_range = [-pow(10,9),pow(10,9)]
    temp = [valid_range]
    while (depth != m and goal != 1):
        if depth == 0:
            print('\nDepth: ', depth)
            check_succerssors_GBFS(temp, ep)
            print('Valid range: ' , valid_range)
        temp = []
        depth += 1
        devided = (abs(valid_range[0])+abs(valid_range[1])) / br
        first = valid_range[0]
        print('\nDepth: ', depth)
        for i in range(0,br):
            temp.append([first, (first + devided)])
            first = temp[-1][-1]
        position, goal = check_succerssors_GBFS(temp, ep)
        valid_range = temp[position]
        print('Valid range: ' , valid_range)
    print('*******************************************')
    if goal == 0:
        print('Root does not found.')
    else:
        print('Answer was it the %d th depth', depth)
    endTime = time.time()
    print('The running time of this algorithm is: ', (endTime-startTime))
    print('*******************************************')

def check_succerssors_GBFS(temp, ep):
    ytemp = []
    eqvars = {'a' : 0.7, 'b' : 10, 'c' : -7.4, 'd' : 10, 'e' : 10}
    goal = 0
    for ranges in temp:
        x = (ranges[0] + ranges[1]) /2
        y = abs(eqvars['a'] * pow(x,7) + eqvars['b'] * pow(x,4) + eqvars['c'] * pow(x,3) + eqvars['d'] * pow(x,2) + eqvars['e'])
        if y < ep and  y > -ep:
            goal = 1
            print('The goal is:' , y)
        ytemp.append(y)
    print('Minimum Y = ', (min(ytemp)))
    return(ytemp.index(min(ytemp)), goal)

def AStar(ep, br, m):
    startTime = time.time()
    print('\n***A* Algorithm with epsilon %5.2f, branching factor %d and depth limit %d:***' %(ep,br,m))
    depth = 0
    goal = 0
    valid_range = [-pow(10,9),pow(10,9)]
    temp = [valid_range]
    while (depth != m and goal != 1):
        if depth == 0:
            print('\nDepth: ', depth)
            check_succerssors_GBFS(temp, ep)
            print('Valid range: ' , valid_range)
            temp = []
        depth += 1
        devided = (abs(valid_range[0])+abs(valid_range[1])) / br
        first = valid_range[0]
        print('\nDepth: ', depth)
        for i in range(0,br):
            temp.append([first, (first + devided)])
            first = temp[-1][-1]
        position, goal = check_succerssors_AStar(temp, ep, depth)
        valid_range = temp[position]
        print('Valid range: ' , valid_range)
    print('*******************************************')
    if goal == 0:
        print('Root does not found.')
    else:
        print('Answer was it the %d th depth', depth)
    endTime = time.time()
    print('The running time of this algorithm is: ', (endTime-startTime))
    print('*******************************************')

def check_succerssors_AStar(temp, ep, g):
    ytemp = []
    eqvars = {'a' : 0.7, 'b' : 10, 'c' : -7.4, 'd' : 10, 'e' : 10}
    goal = 0
    for ranges in temp:
        x = (ranges[0] + ranges[1]) /2
        y = abs(eqvars['a'] * pow(x,7) + eqvars['b'] * pow(x,4) + eqvars['c'] * pow(x,3) + eqvars['d'] * pow(x,2) + eqvars['e'])
        f = y + g
        if y < ep and  y > -ep:
            goal = 1
            print('The goal is:' , y)
        ytemp.append(f)
    print('Minimum Y: ', (min(ytemp)-g))
    return(ytemp.index(min(ytemp)), goal)

#########################################################
GBFS(0.05, 2, 40)
GBFS(0.01, 10, 20)
AStar(0.05, 2, 40)
AStar(0.01, 10, 20)