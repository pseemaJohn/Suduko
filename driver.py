# Program Name : driver.py
# Description : implement and compare AC-3 and Backtracking alogrithm \
# implementing Constraint Propagation, comparing the both for suduko game
# Input Parameter : <input-board>
# <input- board> : is a string 000000000302540000050301070000000004409006005023054790000000050700810000080060009
# Each Sudoku puzzle is represented as a single line of text, which starts from the top-left corner of the board, \
# and enumerates the digits in each tile, row by row. In this assignment, we will use the \
# number zero to indicate tiles that have not yet been filled
# Output Parameter : create / write to a file called output.txt, containing the following statistics:
# output-board: is a string as input but without zero.
# Alogrithm name: a space followed by AC-3 or BTS
# execute as : python3 driver.py 000000000302540000050301070000000004409006005023054790000000050700810000080060009

import math
import sys
import time
from collections import deque
import heapq
from constraintProp import rowNames
from constraintProp import boardSize
from arcConsist import arcConsist
from BTS import BTS

#function: CreateBoard - to convert the input string to dictionary
#input: inpboard - input string
#input: arcObj - an object of CP
#output: a dictionary, which contains key as a combination of row and column, if the value is 0 its replaced with domain (123456789)
def createBoard(inpboard,arcObj):
    outboard = {}
    count = 0
    for i in arcObj.variables:
        if inpboard[count] != '0':
            outboard[i] = inpboard[count]
        else:
            outboard[i] = arcObj.domain
        count += 1
    return outboard

#function: writeoutput - to output the contents to output.txt file
#input: board - the output suduko board
#input: solveType - the type which solved suduko - AC3 or BTS
#output: None
def writeoutput(board,solveType):
        with open("output.txt", "w") as filePtr:
            strtowrite =""
            for str in board.values():
                strtowrite += str
            strtowrite = strtowrite + " " + solveType + "\n"
            filePtr.write(strtowrite)
        return

#function: processBoard - to solve the suduko board
#input: None
#output: None
def processBoard():
    # check argument, if not 2 exit application
    if len(sys.argv) != 2:
        print(" Incorrect Argument provided \n python3 driver.py <board>")
        return 1
    # validate the arguments
    if len(sys.argv[1]) != boardSize:
        print(" Incorrect suduko board")
        return 1
    arcConsObj = arcConsist()

    # capture the board
    board = createBoard(sys.argv[1],arcConsObj)
    #make a copy of board to be used by BTS solver
    BTSboard = board.copy()
    if arcConsObj.processArc(board) == True and arcConsObj.issolved(board):
        writeoutput(board,"AC3")
        print(board)
    else:
        btsObj = BTS()
        outboard = btsObj.processBTS(BTSboard)
        if outboard != False:
            writeoutput(outboard,"BTS")
        else:
            print("Board was not solved by BTS")
            print(BTSboard)

    return 0

# Below line checks if the control of the program is main, __name__ variable provides the name of current process
if __name__ == '__main__':
    processBoard()
