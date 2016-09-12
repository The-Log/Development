import numpy as np
from collections import deque

class sliding_puzzle():
    def __init__(self):
        self.size = 2
        self.puzzle = np.array([[2,1,4],[5,6,8],[4,7, None]])
        self.solution = np.array([[1,2,3],[4,5,6],[7,8, None]])
        self.empty_row = 2
        self.empty_col = 2
    def shift_up(self):
        if(self.empty_row - 1 < 0):
            print('not a vaid move')
            return
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row - 1][self.empty_col]
        self.puzzle[self.empty_row - 1][self.empty_col] = temp
        self.empty_row = self.empty_row - 1
        print("Empty Spot Moved Up:")
        sp.display()
    def shift_down(self):
        if(self.empty_row + 1 > self.size):
            print('not a vaid move')
            return
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row + 1][self.empty_col]
        self.puzzle[self.empty_row + 1][self.empty_col] = temp
        self.empty_row = self.empty_row + 1
        print("Empty Spot Moved Down:")
        sp.display()
    def shift_right(self):
        if(self.empty_col + 1 > self.size):
            print('not a vaid move')
            return
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row][self.empty_col + 1]
        self.puzzle[self.empty_row][self.empty_col + 1] = temp
        self.empty_col = self.empty_col + 1
        print("Empty Spot Moved Right:")
        sp.display()
    def shift_left(self):
        if(self.empty_col - 1 < 0):
            print('not a vaid move')
            return
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row][self.empty_col - 1]
        self.puzzle[self.empty_row][self.empty_col - 1] = temp
        self.empty_col = self.empty_col - 1
        print("Empty Spot Moved Left:")
        sp.display()
    def solve(self):
        visted = set()
        queue = deque()
        while len(queue) != 0:
            if(self.puzzle != self.solution):


    def display(self):
        print(self.puzzle)
        print("")

sp = sliding_puzzle()
print("Original:")
sp.display()
sp.shift_up()
sp.shift_left()
sp.shift_down()
sp.shift_right()
