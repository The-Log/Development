import pickle
import random
import strategy as AI
ai = AI.Strategy()
BLACK_STRATEGY = ai.random_strategy
WHITE_STRATEGY = ai.minimax_strategy(2)

#############################################################
# client.py
# a client to play othello
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
#
# Ankur Mishra: January 2017
############################################################

ROUNDS = 10
SILENT = False

BLACK = AI.core.BLACK
WHITE = AI.core.WHITE
DICT = {}
pickle.dump(DICT, open("DICT.p", "wb"))
#pickle.load("DICT.p")
def play(strategy_BLACK, strategy_WHITE, first=BLACK, silent=True):
    """
    Plays strategy_BLACK vs. strategy_WHITE, beginning with first
    in one game. Returns score as a result (string)
    """
    board = ai.initial_board()
    player = first
    current_strategy = {BLACK: strategy_BLACK, WHITE: strategy_WHITE}
    if not silent:
        print(ai.print_board(board))
    while player is not None:
        move = current_strategy[player](board, player)
        print(move)
        board = ai.make_move(move, player, board)
        player = ai.next_player(board, player)
        if not silent: print(ai.print_board(board))
    DICT.update(ai.get_DICT())
    return ai.score(BLACK, board) # returns "@" "o" or "TIE"


def main():
    """
    Plays ROUNDS Othelo games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """
    points = [0,0,0]
    for i in range(ROUNDS):
        try:
            game_result = play(BLACK_STRATEGY, WHITE_STRATEGY,
                          first=BLACK,
                          silent=SILENT)
            pickle.dump(DICT, open("DICT.p", "wb"))
            print(game_result)
            if(game_result > 0):
                points[0] = points[0] + 1
            elif(game_result < 0):
                points[1] = points[1] + 1
            else:
                points[2] = points[2] + 1
            print('[B,W,T]')
            print(points)
        except ai.IllegalMoveError as e:
            print(e)
    print('[B,W,T]')
    print(points)


if __name__ == "__main__":
    main()
