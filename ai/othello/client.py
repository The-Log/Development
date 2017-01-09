import pickle
import random
import strategy as ai

BLACK_STRATEGY = ai.my_core().human
WHITE_STRATEGY = ai.my_core().random_strategy
#############################################################
# client.py
# a client to play othello
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
#
# Ankur Mishra: January 2017
############################################################

ROUNDS = 1
SILENT = False

BLACK = ai.core.BLACK
WHITE = ai.core.WHITE

def play(strategy_BLACK, strategy_WHITE, first=BLACK, silent=True):
    """
    Plays strategy_BLACK vs. strategy_WHITE, beginning with first
    in one game. Returns score as a result (string)
    """
    board = ai.my_core().initial_board()
    player = first
    current_strategy = {BLACK: strategy_BLACK, WHITE: strategy_WHITE}
    print(ai.my_core().print_board(board))
    while player is not None:
        move = current_strategy[player](board, player)
        board = ai.my_core().make_move(move, player, board)
        player = ai.my_core().next_player(board, player)
        if not silent: print(ai.my_core().print_board(board))
    return ai.my_core().score(BLACK, board) # returns "@" "o" or "TIE"


def main():
    """
    Plays ROUNDS Othelo games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """
    for i in range(ROUNDS):
        try:
            game_result = play(BLACK_STRATEGY, WHITE_STRATEGY,
                          first=random.choice([BLACK, WHITE]),
                          silent=SILENT)
            print(game_result)
            if(game_result > 0):
                print("Black Wins!")
            elif(game_result < 0):
                print("White Wins!")
            else:
                print("Tie!")
        except ai.my_core.IllegalMoveError as e:
            print(e)


if __name__ == "__main__":
    main()
