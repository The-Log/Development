# Ankur Mishra
# Period 7
# 2018amishra@tjhsst.edu
import time
import math
import heapq
import copy
from collections import deque
import random
class nQueens:
    def __init__(self, n):
        '''intializes size and makes an empty list with all choices possible
        '''
        self.size = n
        self.state = [[6,8,2,None,5,None,None,None,None],[None,None,None,None,None,4,None,3,None],[None,None,None,None,None,None,None,None,None],[4,3,None,None,None,8,None,None,None],[None,1,None,None,None,None,2,None,None],[None,None,None,None,None,None,7,None,None],[5,None,None,2,7,None,None,None,None],[None,None,None,None,None,None,None,8,1],[None,None,None,6,None,None,None,None,None]]
        self.choices = [[set(range(1,n+1)) for x in range(n)] for y in range(n)]
        for i in range(self.size):
            for j in range(self.size):
                if(self.state[i][j] != None):
                    self.assign(i, j, self.state[i][j])

    def assign(self, row, col, value):
        '''updates the state by setting state[var] to value
	    also propgates constraints and updates choices
	    '''
        self.state[row][col] = value
        self.choices[row][col] = set()
        for i in range(self.size):
            self.choices[i][col].difference_update({value})
            self.choices[row][i].difference_update({value})
        trow = (row // 3)
        tcol = (col // 3)
        for i in range(3):
            for j in range(3):
                self.choices[3 * trow + i][3 * tcol + j].difference_update({value})
    def goal_test(self):
        '''returns True if state is the goal state
        '''
        for i in range(self.size):
            if(None in self.state[i]):
                return False
        return True
    def get_next_unassigned_var(self):
        '''returns the index of a column that is unassigned and
	    has valid choices available
        '''
        for i in range(self.size):
            if(None not in self.state[i]):
                return None, None
        row = random.randint(0,self.size-1)
        col = random.randint(0,self.size-1)
        if(self.state[row][col] == None):
            return row, col
        else:
            return self.get_next_unassigned_var()
    def get_choices_for_var(self, row, col):
        '''returns choices[var] '''
        return self.choices[row][col]
    def __str__(self):
        '''returns state in string format '''
        return str(self.state)

def dfs_search(start_nQueen):
    ''' sets board as the initial state and returns a
	    board containing an nQueens solution
	    or None if none exists
	'''
    st = time.time()
    num_nodes = 0
    nodes_gen = 0
    frontier = []
    frontier.append(start_nQueen)
    visited = set()
    while(True):
        if(len(frontier) == 0):
            return None
        current = frontier.pop()
        num_nodes = num_nodes + 1
        if(current.goal_test()):
            et = time.time()
            ttime = et - st
            return str(num_nodes) + '\t' + str(nodes_gen) + '\t' + str(current) +'\t' + str(nodes_gen / ttime)+ '\t' + str(ttime)
        row, col = current.get_next_unassigned_var()
        if(row != None and col != None):
            for r in current.choices[col]:
                for val in r:
                    child = nQueens(current.size)
                    child.state = copy.deepcopy(current.state)
                    child.choices = copy.deepcopy(current.choices)
                    child.assign(row, col, val)
                    if(str(child.state) not in visited):
                        nodes_gen = nodes_gen + 1
                        frontier.append(child)
                        visited.add(str(child.state))

b = nQueens(n = 9)
#print(b.choices[0][0])
print(dfs_search(b))
