import othello_core

EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'
PIECES = (EMPTY, BLACK, WHITE, OUTER)
PLAYERS = {BLACK: 'Black', WHITE: 'White'}

# To refer to neighbor squares we can add a direction to a square.
UP, DOWN, LEFT, RIGHT = -10, 10, -1, 1
UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT = -9, 11, 9, -11
DIRECTIONS = (UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT)

class my_core(othello_core):
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

        """
        Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found
        """

        return None

    def is_legal(self, move, player, board):
        if move in legal_moves(player, bloard)
            return True
        else:
            return False


    def make_move(self, move, player, board):
        board[move] = player
        for direction in DIRECTIONS:
            make_flips(move,player, board, direction)
        return board

    def make_flips(self, move, player, board, direction):
        """
        Flip pieces in the given direction as a result of the move by player.
        """
        pass

    def legal_moves(self, player, board):
        """
        Get a list of all legal moves for player, as a list of integers
        """
        pass

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
