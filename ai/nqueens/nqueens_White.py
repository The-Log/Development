import time
from collections import deque
import random

goal_test_counter = 0
contructor_counter = 0
start = 8
end = 400
skip = 1

class nQueens:
    def __init__(self , state=None , choices=None , n=8, parent = None, cursor = 0):
        global contructor_counter
        contructor_counter += 1
        if (choices is None):
            self.choices = [set(range(n)) for i in range(n)]
        else:
            self.choices = choices
        if (state is None ) :
            self.state = [-1] * n
        else:
            self.state= state
        self.n = n
        self.parent = None
        self.cursor = cursor
    def assign(self, var, value):
        if any([i == value for i in self.state]):
            return False
        # propagate row and diagonal constraints
        for i in range(self.n):
            self.choices[i].difference_update({(value + i - var) , (value + var - i) , value})
        # set value
        self.state[var] = value
        self.choices[var] = set()
        self.cursor += 1

        # this used to be in the for loop above -- WRONG!
        for i in range(self.n):
            if len(self.choices[i]) == 1:
                self.assign(i, self.choices[i].pop())
        return True
    def goal_test(self):
        global goal_test_counter
        goal_test_counter += 1
        numassigned = [s != -1 for s in self.state].count(True)
        return numassigned == self.n
    def get_next_unassigned_var(self):
        return self.__getnext_most_constrained()

    def __getnext_most_constrained(self):
        cols = list(range(self.n))
        random.shuffle(cols)
        i_min = cols[0]
        for i in cols:
            if 0 < len(self.choices[i]) < len(self.choices[i_min]) or len(self.choices[i_min]) == 0:
                i_min = i
        return i_min

    def get_choices_for_var(self, var):
        return self.__sort_choices_by_constraints(var)

    def __sort_choices_by_constraints(self, var):
        l = list(self.choices[var])
        l.sort(key = lambda x: abs(x-self.n)//2)
        return l

    def consistency_test(self):
        for i in range(self.n):
            if(self.state[i] == -1 and len(self.choices[i]) == 0):
                return False
        return True

def dfs_recursive(state: nQueens, start_state, count = 0):
    if count > state.n * 3: state, count = start_state, 1
    if state.goal_test(): return state, count+1
    if not state.consistency_test(): return None, count + 1
    var = state.get_next_unassigned_var()
    if state.choices[var] is None: return None, count + 1
    for val in state.get_choices_for_var(var):
        child = nQueens(state = list(state.state), choices = [set(i) for i in state.choices], parent = state, cursor = state.cursor, n = state.n)
        if child.assign(var, val):
            result, subcount = dfs_recursive(child, start_state, count)
            count = subcount
            if result is not None: return result, count + 1
    return None, count + 1

def generate_tests(start, end, skip):
    global goal_test_counter
    global contructor_counter

    outfile = open("results.txt", "a")
    print("*" * 80 , file = outfile)
    header = "DFS with restart"
    title_string = "%4s %10s %10s %8s %8s" % ("n", "goals", "nodes", "time" ,"goals/sec")
    print(header)
    print(header , file = outfile)
    print(title_string)
    print(title_string , file = outfile)

    for size in range( start, end , skip ):
        goal_test_counter = 0
        constructor_counter = 0
        nq = nQueens(n=size)
        start_time = time.time()
        sol, count = dfs_recursive(nq, nq)
        t = time.time() - start_time
        data_line = "%4d %10d %10d %8.3f %8.0f" % (size, goal_test_counter, constructor_counter, t, goal_test_counter / t)

        print(data_line)
        print(data_line, file = outfile)
#if __name__ == "__main__()":
generate_tests(start, end, skip)
