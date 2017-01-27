import random as random
import pickle
import OthelloCore as core
from heapq import heappush
open_slots = set([i for i in range(11, 89) if 1 <= (i % 10) <= 8])
SQUARE_WEIGHTS = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1300, -200, 20, 5, 5, 20, -200, 1200, 0,
    0, -200, -400, -5, -5, -5, -5, -400, -200, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 5, -5, 3, 3, 3, 3, -5, 5, 0,
    0, 20, -5, 15, 3, 3, 15, -5, 20, 0,
    0, -200, -400, -5, -5, -5, -5, -400, -200, 0,
    0, 1200, -200, 20, 5, 5, 20, -200, 1300, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

INF = 100000

#d = pickle.load(open("tree.p", "rb"))
d = {}
move = 0

class Strategy(core.OthelloCore):
    
    #CORE METHODS
    
    def squares(self):
        #op = [i for i in range(11, 89) if 1 <= (i % 10) <= 8]
        return open_slots
    
    def is_valid(self, move):
        """Is move a square on the board?"""
        return move in self.squares()
    
    def opponent(self, player):
        """Get player's opponent piece."""
        if(player == core.WHITE):
            return core.BLACK
        if(player == core.BLACK):
            return core.WHITE
        else:
            return core.EMPTY

    def find_bracket(self, square, player, board, direction):
        """
        Find a square that forms a bracket with `square` for `player` in the given
        `direction`.  Returns None if no such square exists.
        Returns the index of the bracketing square if found
        """
        count = 0
        move = None
        end = False
        curr_pos = square
        if(board[curr_pos+direction] != self.opponent(player)):
            return None
        while(end == False):
            curr_pos += direction
            if(curr_pos > 100 or curr_pos < 0):
                break
            else:
                if(curr_pos % 10 == 0):
                    break
                if(board[curr_pos] == player and count == 0):
                    break
                if(board[curr_pos] == self.opponent(player)):
                    count+=1
                if( (board[curr_pos] == core.EMPTY or board[curr_pos] == player) and count > 0):
                    end = True
                    move = curr_pos
                    break
        return move


    def is_legal(self, move, player, board):
        """Is this a legal move for the player?"""
        moves = []
        if(board[move] == core.EMPTY):
            for i in range(8):    
                m = self.find_bracket(move,player,board,core.DIRECTIONS[i])
                if(m != None):
                    moves.append(m)
            if(len(moves) != 0):
                for i in moves:
                    if(board[i] == player):
                        return True
                    else:
                        continue
        return False

    ### Making moves

    # When the player makes a move, we need to update the board and flip all the
    # bracketed pieces.

    def make_move(self, move, player, board):
        """Update the board to reflect the move by the specified player."""
        board[move] = player

        
        for i in core.DIRECTIONS:
            board = self.make_flips(move, player, board, i)
        
            
        return board

    def make_flips(self, move, player, board, direction):
        """Flip pieces in the given direction as a result of the move by player."""


        moves = []

        pos = move
        count = 0
        while(True):
            pos += direction
            
            if(pos > 100 or pos < 0 or pos % 10 == 0):
                return board
            
            if(board[pos] == player):
                break
            
            if(board[pos] == core.EMPTY):
                return board

            if(board[pos] == self.opponent(player)):
                count+=1
                moves.append(pos)


        for i in moves:
            board[i] = player
        
        return board

    def legal_moves(self, player, board):
        """Get a list of all legal moves for player, as a list of integers"""
        valid_moves = []
        for i in self.squares():
            if(self.is_legal(i, player, board)):
                new_board = board[:]
                new_board = self.make_move(i, player, new_board)
                value = self.weighted_squares(player, new_board)
                #valid_moves.append(i)
                heappush(valid_moves, (value, i))
        validmoves2 = [mo[1] for mo in valid_moves]
        return validmoves2
        #return valid_moves

    def any_legal_move(self, player, board):
        """Can player make any moves? Returns a boolean"""
        for i in self.squares():
            if(self.is_legal(i, player, board)):
                return True
        return False

    def next_player(self,board, prev_player):
        """Which player should move next?  Returns None if no legal moves exist."""
        
        opponentmove = self.any_legal_move(self.opponent(prev_player), board)
        playermove = self.any_legal_move(prev_player, board)

        if(opponentmove == True):
            return self.opponent(prev_player)
        elif(opponentmove == False and playermove == True):
            return prev_player
        elif(opponentmove == False and playermove == False):
            return None
        else:
            return None
        

    def score(self,player, board):
        """Compute player's score (number of player's pieces minus opponent's)."""
        boshal = ''.join(board)
        return ( boshal.count(player) - boshal.count(self.opponent(player)) )

    #END OF CORE METHODS
    

    def human(self, board, player):
        val = int(input("place on spot\t"))        
        while(self.is_legal(val, player, board) != True):
            print("invalid spot")
            val = int(input("try again\t"))
        return val

    def random(self, board, player):
        moves = self.legal_moves(player, board)
        return random.choice(moves)


    def minimax_strategy(self,max_depth):
        def strategy(board, player):
            return self.minimax(board, player, max_depth)
        return strategy

    def minimax(self, board, player, maxdepth):
        if(player == core.BLACK):
            tishal = self.max_dfs(board, player, maxdepth, 0, -INF, INF)[1]
            return tishal
        else:
            tishal = self.min_dfs(board, player, maxdepth, 0, -INF, INF)[1]
            return tishal


    #heuristics

    def weighted_squares(self, player, board):
        weighted_score = 0
        opponent = self.opponent(player)
        for i in self.squares():
            if(board[i] == player):
                weighted_score += SQUARE_WEIGHTS[i]
            if(board[i] == opponent):
                weighted_score -= SQUARE_WEIGHTS[i]
            return weighted_score

    def mobility(self, player, board):
        mh = 0
        blackmoves = len(self.legal_moves(player, board))
        whitemoves = len(self.legal_moves(self.opponent(player), board))
        if(blackmoves < whitemoves):
            mh = 100
        elif(blackmoves + whitemoves != 0):
            mh = 1000*(blackmoves-whitemoves) / (blackmoves + whitemoves)
        else:
            mh = 0
        return mh

    def terminal_eval(self, board):

        blackpcs = board.count(core.BLACK)
        whitepcs = board.count(core.WHITE)

        if(blackpcs > whitepcs):
            return 999
        elif(blackpcs < whitepcs):
            return -999
        else:
            return 0
        

    def parity(self, board, player):
        return self.score(player, board)


    def evaluate(self, player, board):
        return (self.weighted_squares(player, board)) + 10*self.parity(board, player) #+ (1 * self.mobility(player, board)) 


    #end of heuristics

    
    def max_dfs(self, board, player, maxdepth, currdepth, alpha, beta):
        
        if(self.next_player(board, player) == None):
            return self.terminal_eval(board), None
        

        if(currdepth >= maxdepth):
            if(maxdepth % 2 == 0):
                return self.evaluate(player, board), None
            else:
                return self.evaluate(player, board), None

        v = -INF
        move = -1

        childs = self.legal_moves(player, board)
        random.shuffle(childs)

        for m in childs:
            new_board = board[:]
            new_board = self.make_move(m, player, new_board)


            
            if((str(new_board), player) in d):
                new_value = d[(str(new_board), player)]
            else:
                new_value = self.min_dfs(new_board, self.next_player(new_board, player), maxdepth, currdepth+1, alpha, beta)[0]
                #new_value = self.min_dfs(new_board, self.opponent(player), maxdepth, currdepth+1, alpha, beta)[0]
                d[(str(new_board), player)] = new_value
            
            
            #new_value = self.min_dfs(new_board, self.next_player(new_board, player), maxdepth, currdepth+1, alpha, beta)[0]
            
            if(new_value > v):
                v = new_value
                move = m
            
            
            if(v >= beta):
                return v, move
            alpha = max(alpha, v)
            

        return v, move


    def min_dfs(self, board, player, maxdepth, currdepth, alpha, beta):
        
        if(self.next_player(board, player) == None):       
            return self.terminal_eval(board), None
        
        if(currdepth >= maxdepth):
            if(maxdepth % 2 == 0):
                return self.evaluate(player, board), None
            else:
                return self.evaluate(player, board), None

        v = INF
        move = -1

        
        childs = self.legal_moves(player, board)
        random.shuffle(childs)

        for m in childs:
            new_board = board[:]
            new_board = self.make_move(m, player, new_board)

            
            if((str(new_board), player) in d):
                new_value = d[(str(new_board), player)]
            else:
                new_value = self.max_dfs(new_board, self.next_player(new_board, player), maxdepth, currdepth+1, alpha, beta)[0]
                #new_value = self.max_dfs(new_board, self.opponent(player), maxdepth, currdepth+1, alpha, beta)[0]
                d[(str(new_board), player)] = new_value
            
            
            #new_value = self.max_dfs(new_board, self.next_player(new_board, player), maxdepth, currdepth+1, alpha, beta)[0]
            
            if(new_value < v):
                v = new_value
                move = m
            
            
            if(v <= alpha):
                return v, move
            beta = min(beta, v)
            

        return v, move

    def dict_to_pickle(self):
        pickle.dump(d, open("tree.p", "wb"))


