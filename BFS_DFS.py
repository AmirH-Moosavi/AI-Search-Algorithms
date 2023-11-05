# The first BFS implementation function 
def BFS_1():
    frontier = []
    explored = []
    nlen = len(inputGraph[start])
    frontier.append(start)
    Goal = 0
    while Goal == 0:
        temp = frontier[0]
        for i in range(0,nlen):
            if inputGraph[temp][i] != None:
                frontier.append(inputGraph[temp][i])
        explored.append(frontier.pop(0))
        if explored[-1]== end:
            Goal = 1
    print("The shortest path of this graph using the first BFS algoritm:")
    for i in range(len(explored)):
        print('->',explored[i], end =" ")
    # End of the first BFS function
    
# The First DFS implementation function 
def DFS_1():
    Goal = 0
    frontier = []
    explored = []
    nlen = len(inputGraph[start]) + 1
    frontier.append(start)
    while Goal == 0:
        temp = frontier[-1]
        explored.append(frontier.pop())
        for i in range(1,nlen):
            if inputGraph[temp][-i] != None:
                frontier.append(inputGraph[temp][-i])
        if explored[-1] == end:
            Goal = 1
    print("\nThe shortest path of this graph using the first DFS algoritm:")
    for i in range(len(explored)):
        print('->',explored[i], end =" ")
    # End of the first DFS function
    
# The second BFS implementation function
def BFS_2():
    frontier = []
    explored = []
    prev = {}
    prev[start] = None
    frontier.append(start)
    nlen = len(inputGraph[start])
    Goal = 0
    while Goal == 0:
        temp = frontier[0]
        for i in range(0,nlen):
            if inputGraph[temp][i] != None:
                frontier.append(inputGraph[temp][i])
                prev[inputGraph[temp][i]] = frontier[0]
        explored.append(frontier.pop(0))
        if end in frontier:
            Goal = 1
            path = []
            backNode = end
            while backNode != None:
                path.append(backNode)
                backNode = prev[backNode]
    print('\n------------------------------------------------------------------')
    print("The shortest path of this graph using the second BFS algoritm:")
    path.reverse()
    for i in path:
        print('->',i, end =" ")
# End of the second BFS function

# The second DFS implementation function 
def DFS_2():
    Goal = 0
    frontier = []
    explored = []
    prev = {}
    nlen = len(inputGraph[start]) + 1
    prev[start] = None
    frontier.append(start)
    while Goal == 0:
        temp = frontier[-1]
        explored.append(frontier.pop())
        for i in range(1,nlen):
            if inputGraph[temp][-i] != None:
                frontier.append(inputGraph[temp][-i])
                prev[inputGraph[temp][-i]] = temp
        if end in frontier:
            Goal = 1
            backNode = end
            path = []
            while backNode != None:
                path.append(backNode)
                backNode = prev[backNode]
    print("\nThe shortest path of this graph using the second DFS algoritm:")
    path.reverse()
    for i in path:
        print('->',i, end =" ")
    
    # End of the second DFS function

# Input Graph and calling functions
inputGraph = {5 : [3,7],
              3 : [2,4],
              7 : [None,8],
              2 : [None,None],
              4 : [None,8],
              8 : [None,None]}
start = 5
end = 8
BFS_1()
DFS_1()
BFS_2()
DFS_2()





