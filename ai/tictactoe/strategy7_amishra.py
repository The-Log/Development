import random
import math
import core as c

MAX = "X"
MIN = "O"
TIE = "TIE"
INF = math.inf
DICT = dict()

def minimax_strategy(maxd):
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
      new_board = c.make_move(board, player, m)
      if (new_board, player) in DICT:
          new_value = DICT[(new_board, player)]
      else:
          new_value = min_dfs(new_board, c.toggle(player))[0]
          DICT[(new_board, player)] = new_value
      if new_value > v:
          if new_value == 1:
              return new_value, m
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
      new_board = c.make_move(board, player, m)
      if (new_board, player) in DICT:
          new_value = DICT[(new_board, player)]
      else:
          new_value = max_dfs(new_board, c.toggle(player))[0]
          DICT[(new_board, player)] = new_value
      if new_value < v:
          if new_value == -1:
              return new_value, m
          v = new_value
          move = m
  return v, move
