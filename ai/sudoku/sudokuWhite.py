import time
from collections import deque
import random
import copy

goal_test_counter = 0
contructor_counter = 0

board = [[6,-1,2,-1,5,-1,-1,-1,-1],[-1,-1,-1,-1,-1,4,-1,3,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1],[4,3,-1,-1,-1,8,-1,-1,-1],[-1,1,-1,-1,-1,-1,2,-1,-1],[-1,-1,-1,-1,-1,-1,7,-1,-1],[5,-1,-1,2,7,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,8,1],[-1,-1,-1,6,-1,-1,-1,-1,-1]]
class sudoku:
    def __init__(self , state=board , choices=None , n = 9, parent = None, cursor = 0):
        global contructor_counter
        contructor_counter += 1
        if (choices is None):
            self.choices = [[set(range(1,n+1)) for x in range(n)] for y in range(n)]
        else:
            self.choices = choices
        self.state= state
        self.n = n
        for i in range(self.n):
            for j in range(self.n):
                if(self.state[i][j] != -1):
                    self.assign(i, j, self.state[i][j])

        self.parent = None
        self.cursor = cursor

    def assign(self, row, col, value):
        if any([i == value for i in self.state]):
            return False
        # propagate row and diagonal constraints
        self.state[row][col] = value
        self.choices[row][col] = set()

        trow = (row // 3)
        tcol = (col // 3)
        for i in range(3):
            for j in range(3):
                self.choices[3 * trow + i][3 * tcol + j] -= {value}

        for i in range(self.n):
            self.choices[i][col] -= {value}
            self.choices[row][i] -= {value}

        # set value
        #self.cursor = self.cursor + 1

        for i in range(self.n):
            for j in range(self.n):
                if len(self.choices[i][j]) == 1:
                    self.assign(i, j, self.choices[i][j].pop())

        return True

    def goal_test(self):
        global goal_test_counter
        goal_test_counter += 1
        for i in range(self.n):
            if(-1 in self.state[i]):
                return False
        return True

    def get_next_unassigned_var(self):
        return self.__getnext_most_constrained()

    def __getnext_most_constrained(self):
        cols = list(range(self.n))
        rows = list(range(self.n))
        random.shuffle(cols)
        random.shuffle(rows)
        i_min = cols[0]
        j_min = rows[0]
        for i in cols:
            for j in rows:
                if self.state[i][j] == -1 and 0 < len(self.choices[i][j]) < len(self.choices[i_min][j_min]) or len(self.choices[i_min]) == 0:
                    i_min = i
                    j_min = j
        return i_min, j_min

    def get_choices_for_var(self, var):
        return self.__sort_choices_by_constraints(var)

    def __sort_choices_by_constraints(self, var):
        l = list(self.choices[var])
        #l.sort(key = lambda x: abs(x-self.n)//2)
        return l

    def consistency_test(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.state[i][j] == -1 and len(self.choices[i][j]) == 0):
                    return False
        return True

def dfs_recursive(state: sudoku, start_state, count = 0):
    if count > state.n * 3: state, count = start_state, 1
    if state.goal_test(): return state, count+1
    if not state.consistency_test(): return None, count + 1
    row, col = state.get_next_unassigned_var()
    if state.choices[row][col] is None: return None, count + 1
    for r in state.get_choices_for_var(col):
        for val in r:
            child = sudoku(state = list(state.state), choices = copy.deepcopy(state.choices), parent = state, cursor = state.cursor, n = state.n)
            if child.assign(row, col, val):
                result, subcount = dfs_recursive(child, start_state, count)
                count = subcount
                if result is not None: return result, count + 1
    return None, count + 1

def test():
    global goal_test_counter
    global contructor_counter

    outfile = open("results.txt", "a")
    print("*" * 80 , file = outfile)
    title_string = "%10s %10s %8s %8s" % ("goals", "nodes", "time" ,"goals/sec")
    print(title_string)
    print(title_string , file = outfile)
    goal_test_counter = 0
    constructor_counter = 0
    s = sudoku(n=9)
    string = str(s.state)
    start_time = time.time()
    sol, count = dfs_recursive(s, s)
    t = time.time() - start_time
    data_line = "%10d %10d %8.3f %8.0f" % (goal_test_counter, constructor_counter, t, goal_test_counter / t)
    print(data_line)
    print(data_line, file = outfile)
    print("Initial " + str(string))
    #print("End " + str(sol.state))
    for i in sol.state:
        print(i)

test()
