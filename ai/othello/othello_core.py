from core import OthelloCore

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

class my_core(OthelloCore):
    def is_valid(self, move):
        return move in squares()

    def opponent(self, player):
        if (player == WHITE):
            return BLACK
        else:
            return WHITE

    def find_bracket(self, square, player, board, direction):
        bracket = square + direction
        if (board[bracket] == player):
            return None
        enemy = opponent(player)
        while board[bracket] == enemy:
            bracket += direction
        if board[bracket] not in (OUTER, EMPTY):
            return bracket
        else:
            return None

    def is_legal(self, move, player, board):
        if move in legal_moves(player, bloard):
            return True
        else:
            return False

    def make_move(self, move, player, board):
        board[move] = player
        for direction in DIRECTIONS:
            make_flips(move,player, board, direction)
        return board

    def make_flips(self, move, player, board, direction):
        bracket = find_bracket(move, player, board, direction)
        if not bracket:
            return
        square = move + direction
        while square != bracket:
            board[square] = player
            square += direction

    def legal_moves(self, player, board):
        legal_moves = []
        for i in squares():
            legal_moves.add(lambda direction:find_bracket(i, player, board, direction))
        return legal_moves

    def any_legal_move(self, player, board):
        if len(legal_moves(player, board)) == 0:
            return False
        else:
            return True

    def next_player(self,board, prev_player):
        enemy = opponent(prev_player)
        if (any_legal_move(enemy)):
            return enemy
        elif(any_legal_move(prev_player)):
            return prev_player
        return None

    def score(self, player, board):
        p_s, o_s = 0, 0
        enemy = opponent(player)
        for square in squares():
            if board[square] == player:
                p_s = p_s + 1
            elif board[square] == enemy:
                o_s = o_s + 1
        return p_s - o_s
