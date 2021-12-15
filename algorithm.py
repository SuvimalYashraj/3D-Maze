from collections import deque
from queue import PriorityQueue
from node import Node

def findShortestPath(algorithm, stateSpace, start, end, actionGrids, cave):
    # print(stateSpace,start,end,cave)
    actions = cave.get(tuple(start),-1)
    node = Node(start,actions)

    frontier = PriorityQueue()
    expanded = set()

    frontier.put((0,node))

    if algorithm=="BFS":
        return findBFS(stateSpace,start,end,cave,frontier,expanded)

    priority = 0
    futureCost = 0

    while not frontier.empty():
        firstNode = frontier.get()[1]                                                    # remove the node from frontier that needs to be expanded next

        if firstNode.checkSame(end):                                                  # check if goal node is reached
            return firstNode.findPath(start)

        if (firstNode.x,firstNode.y,firstNode.z) in expanded:
            continue
        else:
            expanded.add((firstNode.x,firstNode.y,firstNode.z))                                                    # mark the node once expanded

        # if firstNode.actions==-1:
        #     continue
        possibleNodes = firstNode.getPossibleNodes(stateSpace)                        # according to the available actions, get all possible nodes

        for i in range(len(possibleNodes)):
            if possibleNodes[i] not in expanded:                                       # if possible coordinate is not already expanded, add in frontier
                if cave.get(possibleNodes[i],-1)==-1:
                    continue
                step_cost = firstNode.getCost(possibleNodes[i])
                if algorithm=="A*":
                    futureCost = firstNode.getFutureCost(possibleNodes[i],end)
                priority = step_cost + firstNode.totalCost + futureCost
                frontier.put((priority,Node(possibleNodes[i],cave.get(possibleNodes[i],-1),firstNode,step_cost,priority)))

    return "FAIL"

def findBFS(stateSpace,start,end,cave,frontier,expanded):
    priority = 0
    
    while not frontier.empty():
        priority+=1

        firstNode = frontier.get()[1]                                                    # remove the node from frontier that needs to be expanded next
        # print(firstNode.getCoordinates(),firstNode.actions,firstNode.parent)

        if firstNode.checkSame(end):                                                  # check if goal node is reached
            return firstNode.findPath(start)

        if (firstNode.x,firstNode.y,firstNode.z) in expanded:
            continue
        else:
            expanded.add((firstNode.x,firstNode.y,firstNode.z))                                                    # mark the node once expanded
        # print(expanded)

        # if firstNode.actions==-1:
        #     continue
        possibleNodes = firstNode.getPossibleNodes(stateSpace)                        # according to the available actions, get all possible nodes
        # print(possibleNodes)
        for i in range(len(possibleNodes)):
            if possibleNodes[i] not in expanded:                                       # if possible coordinate is not already expanded, add in frontier
                if cave.get(possibleNodes[i],-1)==-1:
                    continue
                frontier.put((priority,Node(possibleNodes[i],cave.get(possibleNodes[i],-1),firstNode,1)))
                priority+=1
    
    return "FAIL"
