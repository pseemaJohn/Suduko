from constraintProp import constraintProp
from collections import deque

class arcConsist(constraintProp):

    def processArc(self,board):
        count = 0
        processQ = deque()
        for i in self.constraints.keys():
            for val in self.constraints[i]:
                processQ.append((i,val))
        while len(processQ) != 0:
            own,neigh = processQ.popleft()
            count+=1
            values = board[own]
            for xi in values:
                if not self.makeArcConsistent(xi,board[neigh]):
                    board[own] = board[own].replace(xi, '')
                    if len(board[own]) == 0:
                        return False
                    for peer in self.constraints[own]:
                        if peer != neigh:
                            processQ.append((peer,own))
        return True


    def makeArcConsistent(self,xi,neighValues):
        for xj in neighValues:
            if xj != xi:
                return True
        return False










