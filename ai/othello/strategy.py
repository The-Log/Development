import othello_core as core
import random

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

class my_core(core.OthelloCore):
    def initial_board(self):
        """Create a new board with the initial black and white positions filled."""
        board = [OUTER] * 100
        for i in self.squares():
            board[i] = EMPTY
        # The middle four squares should hold the initial piece positions.
        board[44], board[45] = WHITE, BLACK
        board[54], board[55] = BLACK, WHITE
        return board

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
        if move in self.legal_moves(player, bloard):
            return True
        else:
            return False

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
        legal_moves = []
        for i in self.squares():
            legal_moves.append(lambda direction:self.find_bracket(i, player, board, direction))
        return legal_moves

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
        for square in squares():
            if board[square] == player:
                p_s = p_s + 1
            elif board[square] == enemy:
                o_s = o_s + 1
        return p_s - o_s

    def minimax_strategy(self, max_depth):
        pass

    def human(self, board, player):
        move = int(input("Your move?"))
        while(move in self.legal_moves(player, board)):
            move = int(input("Your move?"))
        return move

    def random_strategy(self, board, player):
        l = self.legal_moves(player, board)
        r = random.randint(0, len(l))
        return r
