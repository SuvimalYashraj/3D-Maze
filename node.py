
from collections import deque

class Node:
    def __init__(self,coordinates,actions,parent=None,cost=0,totalCost=0) -> None:
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.actions = actions
        self.parent = parent
        self.cost = cost
        self.totalCost = totalCost

    #Dictionary for encoded actions
    actionCoordinates = {
        1: [1,0,0],
        2: [-1,0,0],
        3: [0,1,0],
        4: [0,-1,0],
        5: [0,0,1],
        6: [0,0,-1],
        7: [1,1,0],
        8: [1,-1,0],
        9: [-1,1,0],
        10: [-1,-1,0],
        11: [1,0,1],
        12: [1,0,-1],
        13: [-1,0,1],
        14: [-1,0,-1],
        15: [0,1,1],
        16: [0,1,-1],
        17: [0,-1,1],
        18: [0,-1,-1]
        }

    def getPossibleNodes(self, bound):
        possibleNodes = []
        for i in range(len(self.actions)):
            x = self.x + self.actionCoordinates.get(self.actions[i])[0]
            y = self.y + self.actionCoordinates.get(self.actions[i])[1]
            z = self.z + self.actionCoordinates.get(self.actions[i])[2]
            if x>=0 and x<bound[0] and y>=0 and y<bound[1] and z>=0 and z<bound[2]:
                possibleNodes.append((x,y,z))
        return possibleNodes

    def getCoordinates(self):
        return (self.x,self.y,self.z)

    def getActions(self):
        return self.actions
    
    def checkSame(self, goalNode):
        if self.x == goalNode[0] and self.y == goalNode[1] and self.z == goalNode[2]:
            return True
        return False

    def findPath(self, start):
        node = self
        path = deque()
        cost = 0
        while not node.checkSame(start):
            cost += node.cost
            path.appendleft((node.getCoordinates(),node.cost))
            node = node.parent
        path.appendleft((node.getCoordinates(),0))
        return cost,len(path),path

    def getCost(self, currNode):
        if abs(self.x-currNode[0])+abs(self.y-currNode[1])+abs(self.z-currNode[2])==2:
            return 14
        else:
            return 10

    def getFutureCost(self,nextNode,goalNode):
        cost = pow(pow(abs(nextNode[0]-goalNode[0]),2)+pow(abs(nextNode[1]-goalNode[1]),2)+pow(abs(nextNode[2]-goalNode[2]),2),1/2)*10
        return cost

    def __lt__(self,other):
        if not isinstance(other, type(self)):
            raise NotImplementedError("Only available for Node Node comparison")
        if self.x<=other.x:
            return True

    def __repr__(self) -> str:
        return f"Node({(self.x, self.y, self.z)}, {self.actions})"
