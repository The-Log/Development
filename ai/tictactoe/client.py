from server import *

board = tictactoe()
print(board.display())

numberboard = tictactoe()
numberboard.state = ['1','2','3','4','5','6','7','8','9']
print("Choose a number 1 through 9 which correspond to the board")
print("")
print(numberboard.display())

while(board.goal_test() == False):
    print()
    value = input()
    board.assign(int(value))
    print(board.display())
