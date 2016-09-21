import copy
from collections import deque
from time import time
visited = set()
class node():
    def __init__(self, parent = None, puzzle = [[6,4,5],[2,7,3],[8,1,None]], depth = 0 ):
        self.parent = parent
        self.puzzle = puzzle
        if(self.puzzle == None):
            return
        for i in range (len(puzzle)):
            for j in range(len(puzzle[i])):
                if(puzzle[i][j] == None):
                    self.empty_row = i
                    self.empty_col = j
        self.depth = depth
    def get_children(self, frontier):
        children = []
        parent = self
        up = node(parent, self.up(), self.depth + 1)
        down = node(parent, self.down(), self.depth + 1)
        left = node(parent, self.left(), self.depth + 1)
        right = node(parent, self.right(), self.depth + 1)

        if(up.puzzle != None and str(up) not in visited):
            children.append(up)
            frontier.append(up)
            visited.add(str(up))
        if(down.puzzle != None and str(down) not in visited):
            children.append(down)
            frontier.append(down)
            visited.add(str(down))
        if(left.puzzle != None and str(left) not in visited):
            children.append(left)
            frontier.append(left)
            visited.add(str(left))
        if(right.puzzle != None and str(right) not in visited):
            children.append(right)
            frontier.append(right)
            visited.add(str(right))
        return children

    def down(self):
        if(self.empty_row - 1 < 0):
            return None
        s = copy.deepcopy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row-1][self.empty_col]
        s[self.empty_row-1][self.empty_col] = temp
        return s
    def up(self):
        if(self.empty_row + 1 > 2):
            return None
        s = copy.deepcopy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row+1][self.empty_col]
        s[self.empty_row+1][self.empty_col] = temp
        return s
    def right(self):
        if(self.empty_col - 1 < 0):
            return None
        s = copy.deepcopy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row][self.empty_col -1]
        s[self.empty_row][self.empty_col-1] = temp
        return s
    def left(self):
        if(self.empty_col + 1 > 2):
            return None
        s = copy.deepcopy(self.puzzle)
        temp = s[self.empty_row][self.empty_col]
        s[self.empty_row][self.empty_col] = s[self.empty_row][self.empty_col+1]
        s[self.empty_row][self.empty_col+1] = temp
        return s

    def display(self):
        if(self.puzzle == None):
            return ""
        s = [[str(e) for e in row] for row in self.puzzle]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        string = '\n'.join(table)
        string = "\n" + string + "\n"
        return string

    def get_path(self):
        print("I got here!")
        path = []
        while(self != None):
            path.append(self)
            self = self.parent
        path.reverse()
        return path

    def __str__(self):
        if(self.puzzle == None):
            return ""
        return str(self.puzzle)
st = time()
sp = node()
goal = node(None,[[1,2,3],[4,5,6],[7,8, None]])

def search():
    frontier = deque()
    frontier.append(sp)
    while(True):
        if(len(frontier) == 0):
            return None
        current = frontier.popleft()
        if(current.display() ==  goal.display()):
            return current.get_path()
        current.get_children(frontier)

listA = search()
for i in listA:
    print(i.display())
print("Time it took: " + str(time() - st))
