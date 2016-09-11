import numpy as np

class sliding_puzzle():
    def __init__(self):
        self.puzzle = np.array([[2,1,4],[5,6,8],[4,7,0]])
        self.empty_row = 2
        self.empty_col = 2
    def shift_up(self):
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row - 1][self.empty_col]
        self.puzzle[self.empty_row - 1][self.empty_col] = temp
        self.empty_row = self.empty_row - 1
        print("Empty Spot Moved Up:")
        sp.display()
    def shift_down(self):
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row + 1][self.empty_col]
        self.puzzle[self.empty_row + 1][self.empty_col] = temp
        self.empty_row = self.empty_row + 1
        print("Empty Spot Moved Down:")
        sp.display()
    def shift_right(self):
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row][self.empty_col + 1]
        self.puzzle[self.empty_row][self.empty_col + 1] = temp
        self.empty_col = self.empty_col + 1
        print("Empty Spot Moved Right:")
        sp.display()
    def shift_left(self):
        temp = self.puzzle[self.empty_row][self.empty_col]
        self.puzzle[self.empty_row][self.empty_col] = self.puzzle[self.empty_row][self.empty_col - 1]
        self.puzzle[self.empty_row][self.empty_col - 1] = temp
        self.empty_col = self.empty_col - 1
        print("Empty Spot Moved Left:")
        sp.display()
    def display(self):
        print(self.puzzle)
        print("")

sp = sliding_puzzle()
print("Original:")
sp.display()
sp.shift_up()
sp.shift_left()
