# Ankur Mishra
# Period 7
# 2018amishra@tjhsst.edu
import time
import math
import random

x = 'X'
o = 'O'
class tictactoe:
    def __init__(self, turn):
        self.size = 9
        self.state = ['-'] * self.size
        self.turn = turn
    def assign(self, var, value):
        if(self.state[var] == '-'):
            self.state[var] = value

    def goal_test(self):
        if('-' not in self.state):
            return True
        if(self.state[0] != '-' and self.state[0]  == self.state[4] == self.state[8]):
            return True
        if(self.state[2] != '-' and self.state[2]  == self.state[4] == self.state[6]):
            return True
        for i in range(3):
            i = i * 3
            if(self.state[i] != '-' and self.state[i] == self.state[i+1] == self.state[i+2]):
                return True
        for i in range(3):
            if(self.state[i] != '-' and self.state[i] == self.state[i+3] == self.state[i+6]):
                return True
        else:
            return False

    def get_children(self):
        childrens =[]
        if self.goal_test():
            return childrens
        for i in range(self.size):
            if(self.state[i] == '-'):
                if(self.turn == x):
                    child = tictactoe(o)
                    child.state = list(self.state)
                    child.assign(i, x)
                    childrens.append(child)
                else:
                    child = tictactoe(x)
                    child.state = list(self.state)
                    child.assign(i, o)
                    childrens.append(child)
        return childrens

    def __str__(self):
        return str(self.state)

    def get_2d_board(self):
        s = ''
        for i in range(self.size):
            s = s + '{:4}'.format(self.state[i])
            if((i + 1) % 3 == 0):
                s = s + "\n"
        return s

def dfs_search(start_tictactoe):
    allBoards = set()
    frontier = [start_tictactoe]
    visited = set()
    while(True):
        if(len(frontier) == 0):
            return allBoards
        current = frontier.pop()
        if(current.goal_test()):
            allBoards.add(current)
        children = current.get_children()
        for i in children:
            if str(i.state) not in visited:
                frontier.append(i)
                visited.add(str(i.state))

t = tictactoe(x)
start = time.time()
sol = dfs_search(t)
end = time.time()
print(len(sol))
print(end - start)
