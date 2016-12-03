import random
import time
x = 'x'
o = 'o'
class tictactoe:
    def __init__(self, turn = x , p_value = x, c_value = o):
        self.size = 9
        self.state = ['-'] * self.size
        self.turn = turn
        self.p_value = p_value
        self.c_value = c_value

    def assign(self, var):
        var = var - 1
        if(self.state[var] == '-'):
            self.state[var] = self.p_value
        else:
            print("\nNot Valid Move!")
            return
        if('-' not in self.state):
            print("\nIt's a tie!")
            return
        if(self.goal_test()):
            print("\nYou won!")
            return
        r = random.randint(0,self.size-1)
        while (self.state[r] != '-'):
            r = random.randint(0,self.size-1)
        self.state[r] = self.c_value
        if(self.goal_test()):
            print("\nYou lost!")
            return

    def goal_test(self):
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

    def display(self):
        s = ''
        for i in range(self.size):
            s = s + '{:4}'.format(self.state[i])
            if((i + 1) % 3 == 0):
                s = s + "\n"
        return s

    def __str__(self):
        return str(self.state)
