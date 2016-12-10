import random
import math
import core as c

MAX = "X"
MIN = "O"
TIE = "TIE"
INF = math.inf

def minimax_strategy():
    def strategy(board, player):
        return minimax(board, player)
    return strategy

def human(board, player):
    move = int(input("Your move? "))
    return move

def random_strategy(board, player):
    move = random.randint(0,8)
    if('.' not in board):
        return
    if(board[move] == '.'):
        return move
    else:
        return random_strategy(board, player)

def minimax(board, player):
    if player == MAX:
        move = max_dfs(board, player)[1]
    if player == MIN:
        move = min_dfs(board, player)[1]
    return move

def max_dfs(board, player):
  if c.terminal_test(board) and c.winner(board) == MAX:
      return 1, None
  if c.terminal_test(board) and c.winner(board) == MIN:
      return -1, None
  if c.terminal_test(board) and c.winner(board) == None:
      return 0, None
  v = -INF
  move = -1
  for m in c.actions(board):
      new_value = min_dfs(c.make_move(board, player, m), c.toggle(player))[0]
      if new_value > v:
          v = new_value
          move = m
  return v, move

def min_dfs(board, player):
  if c.terminal_test(board) and c.winner(board) == MAX:
      return 1, None
  if c.terminal_test(board) and c.winner(board) == MIN:
      return -1, None
  if c.terminal_test(board) and c.winner(board) == None:
      return 0, None
  v = INF
  move = -1
  for m in c.actions(board):
      new_value = max_dfs(c.make_move(board, player, m), c.toggle(player))[0]
      if new_value < v:
          v = new_value
          move = m
  return v, move
