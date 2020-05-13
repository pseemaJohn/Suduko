from constraintProp import constraintProp
from copy import deepcopy

class BTS(constraintProp):
    def __init__(self):
        super(BTS, self).__init__()
        self.assignment = dict()

    def processBTS(self,board):
        self.identifyConstAndApply(board)
        return self.backtrack(board)

#for i in self.assignDomainVal(var):
#if val == assignment constraints:
#add val to assignment
#result = backtrack
#if result:
#return result
#remove val from assignment
#return False
    def backtrack(self,board):
        if self.issolved(board):
            return board

        # identify the variable with lots domain value
        var = self.getMinimumValueVar(board)
        #make a copy of board to reassign in case of backtrack
        #tempboard = deepcopy(board)
        boardVal = board[var]
        for minVarDomVal in boardVal:
            #before assigning the value check if it matches the constraint.
            if self.checkConstraint(minVarDomVal,var):
                tempboard = board.copy()
                board[var] = self.assignment[var] = minVarDomVal
                if self.forwardCheck(var,minVarDomVal,board) == True:
                    outboard = self.backtrack(board)
                    if outboard != False:
                        return outboard
                self.assignment.pop(var)
                board = tempboard

        return False



    def identifyConstAndApply(self,grid):
        for val in grid:
            if len(grid[val]) == 1:
                self.assignment[val] = grid[val]
                for peer in self.constraints[val]:
                    #if grid[val] in grid[peer]:
                    grid[peer] = grid[peer].replace(grid[val], '')
        return

    def getMinimumValueVar(self,grid):
        lowlen = 10
        retVar = None
        for val in grid:
            tmplen = len(grid[val])
            if val not in self.assignment.keys() and tmplen < lowlen:
                lowlen = tmplen
                retVar = val
        return retVar

    def forwardCheck(self,own,val,board):
        for peer in self.constraints[own]:
            if peer not in self.assignment.keys() and val in board[peer]:
                if len(board[peer]) == 1:
                    return False
                board[peer] = board[peer].replace(val, '')
                if len(board[peer]) == 1:
                    if self.forwardCheck(peer,board[peer],board) == False:
                        return False
        return True

    def checkConstraint(self,val,var):
        for neigh in self.constraints[var]:
            if neigh in self.assignment.keys() and self.assignment[neigh] == val:
                return False
        return True


