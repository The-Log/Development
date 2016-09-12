import numpy as np
from collections import deque

class sliding_puzzle():
    def __init__(self):
        self.size = 2
        self.puzzle = np.array([[2,1,4],[5,6,8],[4,7, None]])
        self.solution = np.array([[1,2,3],[4,5,6],[7,8, None]])
        self.empty_row = 2
        self.empty_col = 2
    def get_puzzle(self):
        return self.puzzle
    def shift_up(self):
        if(self.empty_row - 1 < 0):
            return None
        s = np.copy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row - 1][self.empty_col]
        s[self.empty_row - 1][self.empty_col] = temp
        return s
    def shift_down(self):
        if(self.empty_row + 1 > self.size):
            return None
        s = np.copy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row + 1][self.empty_col]
        s[self.empty_row + 1][self.empty_col] = temp
        return s
    def shift_right(self):
        if(self.empty_col + 1 > self.size):
            return None
        s = np.copy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row][self.empty_col + 1]
        s[self.empty_row][self.empty_col + 1] = temp
        return s
    def shift_left(self):
        if(self.empty_col - 1 < 0):
            return None
        s = np.copy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row][self.empty_col - 1]
        s[self.empty_row][self.empty_col - 1] = temp
        return s
    def display(self):
        print(self.puzzle)
        print("")
    def solve(self):
        visted = set()
        queue = deque()
        queue.append(self.puzzle)
        while len(queue) != 0:
            self.display()
            if np.array_equal(self.puzzle, self.solution):
                return self.puzzle
            if(self.shift_right() not in visted):
                queue.append(self.shift_right())
                visted.add(self.shift_right())
            if(self.shift_left() not in visted):
                queue.append(self.shift_left())
                visted.add(self.shift_left())
            if(self.shift_up() not in visted):
                queue.append(self.shift_up())
                visted.add(self.shift_up())
            if(self.shift_down() not in visted):
                queue.append(self.shift_down())
                visted.add(self.shift_down())
            self.puzzle = queue.pop()
        return None

sp = sliding_puzzle()
print("Original:")
sp.display()
print("Solution:")
print(sp.solve())
