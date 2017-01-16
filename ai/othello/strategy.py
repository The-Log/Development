import othello_core as core
import random


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

class my_core(core.OthelloCore):
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
        hasbracket = lambda direction: self.find_bracket(move, player, board, direction)
        return board[move] == EMPTY and any(map(hasbracket, DIRECTIONS))

    def make_move(self, move, player, board):
        board[move] = player
        for direction in DIRECTIONS:
            self.make_flips(move,player, board, direction)
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

    def score(self, player, board):
        p_s, o_s = 0, 0
        enemy = self.opponent(player)
        for square in self.squares():
            if board[square] == player:
                p_s = p_s + 1
            elif board[square] == enemy:
                o_s = o_s + 1
        return p_s - o_s

    def minimax_strategy(self, board, player):
        if player == BLACK:
            move = self.max_dfs(board, player)[1]
        if player == WHITE:
            move = self.min_dfs(board, player)[1]
        return move

    def max_dfs(self, board, player):
        if '.' not in board and self.winner(board, player) == WHITE:
            return -1
        if '.' not in board and self.winner(board, player) == BLACK:
            return 1
        if '.' not in board and self.winner(board, player) == None:
            return 0
        v = -INF
        for m in self.legal_moves(board, player):
            new_board = self.make_move(board, player, m)
            if (new_board, player) in DICT:
                new_value = DICT[(new_board, player)]
            else:
                if self.any_legal_move(self.opponent(player)):
                    new_value = self.min_dfs(new_board, self.opponent(player))[0]
                    DICT[(new_board, player)] = new_value
                else:
                    new_value = self.max_dfs(new_board, player)[0]
                    DICT[(new_board, player)] = new_value
            if new_value > v:
                if new_value == 1:
                    return new_value, m
                v = new_value
                move = m
        return v, move

    def min_dfs(self, board, player):
        self.evaluate(board, player)
        v = INF
        for m in self.legal_moves(board):
            new_board = self.make_move(board, player, m)
            if (new_board, player) in DICT:
                new_value = DICT[(new_board, player)]
            else:
                if self.any_legal_move(self.opponent(player)):
                    new_value = self.max_dfs(new_board, self.opponent(player))[0]
                    DICT[(new_board, player)] = new_value
                else:
                    new_value = self.min_dfs(new_board, player)[0]
                    DICT[(new_board, player)] = new_value
            if new_value < v:
                if new_value == 1:
                    return new_value, m
                v = new_value
                move = m
        return v, move

    def evaluate(self, board, player):
        #if '.' not in board and self.winner(board, player) == WHITE:
        #    return -1
        #if '.' not in board and self.winner(board, player) == BLACK:
        #    return 1
        #if '.' not in board and self.winner(board, player) == None:
        #    return 0
        score = 0
        for i in len(board):
            if board[i] == player:
                score = score + SQUARE_WEIGHTS[i]
            elif board[i] == self.opponent(player):
                score = score - SQUARE_WEIGHTS[i]
        return score

    def winner(self, board, player):
        if self.score(board, player) > 0:
            return BLACK
        elif self.score(board, player) < 0:
            return WHITE
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
