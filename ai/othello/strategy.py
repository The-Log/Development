import Othello_Core as core
import random
import math

#############################################################
# strategy.py
# implements core methods to play othello
# imports methods from "othello_core.py" as core
#
# Ankur Mishra: January 2017
############################################################

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)
DICT = dict()
INF = float('Inf')

SQUARE_WEIGHTS = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, -20, -40, -5, -5, -5, -5, -40, -20, 0,
    0, 120, -20, 20, 5, 5, 20, -20, 120, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

MAX_VALUE = sum(map(abs, SQUARE_WEIGHTS))
MIN_VALUE = -MAX_VALUE

class Strategy(core.OthelloCore):
    def is_valid(self, move):
        return move in self.squares()

    def opponent(self, player):
        if (player == WHITE):
            return BLACK
        else:
            return WHITE

    def find_bracket(self, square, player, board, direction):
        bracket = square + direction
        if (board[bracket] == player):
            return None
        enemy = self.opponent(player)
        while board[bracket] == enemy:
            bracket += direction
        if board[bracket] not in (OUTER, EMPTY):
            return bracket
        else:
            return None

    def is_legal(self, move, player, board):
        b = lambda direction: self.find_bracket(move, player, board, direction)
        return board[move] == EMPTY and any(map(b, DIRECTIONS))

    def make_move(self, move, player, board):
        #print(player)
        board[int(move)] = player
        for direction in DIRECTIONS:
            self.make_flips(move, player, board, direction)
        return board

    def make_flips(self, move, player, board, direction):
        bracket = self.find_bracket(move, player, board, direction)
        if not bracket:
            return
        square = move + direction
        while square != bracket:
            board[square] = player
            square += direction

    def legal_moves(self, player, board):
        lm = []
        for s in self.squares():
            if self.is_legal(s, player, board):
                lm.append(s)
        return lm

    def any_legal_move(self, player, board):
        if len(self.legal_moves(player, board)) == 0:
            return False
        else:
            return True

    def next_player(self,board, prev_player):
        enemy = self.opponent(prev_player)
        if (self.any_legal_move(enemy, board)):
            return enemy
        elif(self.any_legal_move(prev_player, board)):
            return prev_player
        return None


    def best_strategy(self, player, board, best_move, still_running):
        max_depth = 1
        while(still_running.value != 0):
            ai = self.alphabeta_strategy(max_depth)
            best_move.value = ai(board, player)
            max_depth = max_depth + 1

    def alphabeta_strategy(self, max_depth):
        def strategy(board, player):
            return self.minimax_ab(board, player, max_depth, -INF, INF)
        return strategy

    def minimax_ab(self, board, player, max_depth, a, b):
        if (max_depth % 2 == 0):
            move = self.max_dfs_ab(board, player, max_depth, a, b)[1]
        if (max_depth % 2 == 1):
            move = self.min_dfs_ab(board, player, max_depth, a, b)[1]
        return move

    def max_dfs_ab(self, board, player, depth, a, b):
        if depth == 0:
            return self.evaluate(board, player), None
        if self.any_legal_move(player, board) == False and self.any_legal_move(self.opponent(player), board) == False:
            if self.winner(board, player) == player:
                return INF, None
            if self.winner(board, player) == self.opponent(player):
                return -INF, None
            if self.winner(board, player) == None:
                return 0, None
        v = -INF
        lm = self.legal_moves(player, board)
        move = lm[0]

        for m in lm:
            new_board = list(board)
            new_board = self.make_move(m, player, new_board)
            if (str(new_board), player) in DICT:
                new_value = DICT[(str(new_board), player)]
            else:
                if(self.next_player(new_board, player) == self.opponent(player)):
                    new_value = self.min_dfs_ab(new_board, self.next_player(new_board, player), depth - 1, a , b)[0]
                    DICT[(str(new_board), player)] = new_value
                else:
                    new_value = self.max_dfs_ab(new_board, self.next_player(new_board, player), depth - 1, a , b)[0]
                    DICT[(str(new_board), player)] = new_value
            if new_value > v:
                v = new_value
                move = m
            if v >= b:
                return v, m
            a = max(a,v)
        return v, move

    def min_dfs_ab(self, board, player, depth, a, b):
        if depth == 0:
            return self.evaluate(board, player), None
        if self.any_legal_move(player, board) == False and self.any_legal_move(self.opponent(player), board) == False:
            if self.winner(board, player) == player:
                return -INF, None
            if self.winner(board, player) == self.opponent(player):
                return INF, None
            if self.winner(board, player) == None:
                return 0, None
        v = INF
        lm = self.legal_moves(player, board)
        move = lm[0]

        for m in lm:
            new_board = list(board)
            new_board = self.make_move(m, player, new_board)
            if (str(new_board), player) in DICT:
                new_value = DICT[(str(new_board), player)]
            else:
                if self.any_legal_move(self.opponent(player), new_board):
                    new_value = self.max_dfs_ab(new_board, self.opponent(player), depth - 1, a, b)[0]
                    DICT[(str(new_board), player)] = new_value
                else:
                    new_value = self.min_dfs_ab(new_board, player, depth - 1, a, b)[0]
                    DICT[(str(new_board), player)] = new_value
            if new_value < v:
                v = new_value
                move = m
            if v <= a:
                return v, m
            b = min(b,v)
        return v, move

    def minimax_strategy(self, max_depth):
        def strategy(board, player):
            return self.minimax(board, player, max_depth)
        return strategy

    def minimax(self, board, player, depth):
        if (depth % 2 == 0):
            move = self.max_dfs(board, player, depth)[1]
        if (depth % 2 == 1):
            move = self.min_dfs(board, player, depth)[1]
        return move

    def max_dfs(self, board, player, depth):
        if depth == 0:
            return self.evaluate(board, player), None
        if self.any_legal_move(player, board) == False and self.any_legal_move(self.opponent(player), board) == False:
            if self.winner(board, player) == player:
                return MIN_VALUE * self.evaluate(board, player), None
            if self.winner(board, player) == self.opponent(player):
                return MAX_VALUE * self.evaluate(board, player), None
            if self.winner(board, player) == None:
                return 0, None
        v = -INF
        lm = self.legal_moves(player, board)
        move = lm[0]

        for m in lm:
            new_board = list(self.make_move(m, player, board))
            if (str(new_board), player) in DICT:
                new_value = DICT[(str(new_board), player)]
            else:
                if(self.next_player(new_board, player) == self.opponent(player)):
                    new_value = self.min_dfs(new_board, self.next_player(new_board, player), depth - 1)[0]
                    DICT[(str(new_board), player)] = new_value
                else:
                    new_value = self.max_dfs(new_board, self.next_player(new_board, player), depth - 1)[0]
                    DICT[(str(new_board), player)] = new_value
            if new_value > v:
                v = new_value
                move = m
        return v, move

    def min_dfs(self, board, player, depth):
        if depth == 0:
            return self.evaluate(board, player), None
        if self.any_legal_move(player, board) == False and self.any_legal_move(self.opponent(player), board) == False:
            if self.winner(board, player) == player:
                return MIN_VALUE * self.evaluate(board, player), None
            if self.winner(board, player) == self.opponent(player):
                return MAX_VALUE * self.evaluate(board, player), None
            if self.winner(board, player) == None:
                return 0, None
        v = INF
        lm = self.legal_moves(player, board)
        if len(lm) == 0:
            print(lm)
        move = lm[0]
        for m in lm:
            new_board = list(self.make_move(m, player, board))
            if (str(new_board), player) in DICT:
                new_value = DICT[(str(new_board), player)]
            else:
                if self.any_legal_move(self.opponent(player), new_board):
                    new_value = self.max_dfs(new_board, self.opponent(player), depth - 1)[0]
                    DICT[(str(new_board), player)] = new_value
                else:
                    new_value = self.min_dfs(new_board, player, depth - 1)[0]
                    DICT[(str(new_board), player)] = new_value
            if new_value < v:
                v = new_value
                move = m
        return v, move

    def score(self, player, board):
        p, o = 0, 0
        opponent = self.opponent(player)
        for square in board:
            if square == player:
                p = p + 1
            elif square == opponent:
                o = o + 1
        return p - o

    def evaluate(self, board, player):
        score = 0
        for i in range(len(board)):
            if board[i] == player:
                score = score + SQUARE_WEIGHTS[i]
            elif board[i] == self.opponent(player):
                score = score - SQUARE_WEIGHTS[i]
        return score

    def winner(self, board, player):
        if self.score(player, board) > 0:
            return player
        elif self.score(player, board) < 0:
            return self.opponent(player)
        else:
            return None

    def human(self, board, player):
        move = int(input("Your move?\n"))
        lm = self.legal_moves(player, board)
        while(move not in lm):
            print("Invalid move! Choose one of these, if you need help.")
            print(lm)
            move = int(input(""))
        return move

    def random_strategy(self, board, player):
        lm = self.legal_moves(player, board)
        r = random.randint(0, len(lm) - 1)
        #print("Computer chose: " + str(lm[r]))
        return lm[r]
    def get_DICT(self):
        return DICT
