import pickle
import random
import strategy as ai

BLACK_STRATEGY = ai.my_core().human
WHITE_STRATEGY = ai.my_core().random_strategy
#############################################################
# client.py
# a simple tic-tac-toe client
# plays 2 strategies against each other and keeps score
# imports strategies from "strategies.py" as ai
# rest of functionality is stored in core.py
#
# Patrick White: December 2016
############################################################

ROUNDS = 1
SILENT = False

BLACK = ai.core.BLACK
WHITE = ai.core.WHITE

def play(strategy_BLACK, strategy_WHITE, first=BLACK, silent=True):
    """
    Plays strategy_BLACK vs. strategy_WHITE, beginning with first
    in one game. Returns @, o or TIE as a result (string)

    The functions make_move, next_player and terminal_test are
    implemented elsewhere (e.g. in core.py). The current implementation
    uses a 9-char string as the state, but that is not exposed at this level.
    """
    board = ai.my_core().initial_board()
    player = first
    current_strategy = {BLACK: strategy_BLACK, WHITE: strategy_WHITE}
    print(player)
    print(ai.my_core().print_board(board))
    while player is not None:
        move = current_strategy[player](board, player)
        board = ai.my_core().make_move(move, player, board)
        player = ai.my_core().next_player(board, player)
        print(player)
        if not silent: print(ai.my_core().print_board(board))
    return terminal_test(board) # returns "@" "o" or "TIE"


def main():
    """
    Plays ROUNDS tic-tac-toe games and keeps a count of
    wins/ties. Uses strategies defined as global constants above.
    Selects a random starting player
    """
    j = []
    for i in range(ROUNDS):
        try:
            game_result = play(BLACK_STRATEGY, WHITE_STRATEGY,
                          first=random.choice([BLACK, WHITE]),
                          silent=SILENT)
            j.append(game_result)
            print("Winner: ", game_result)
        except ai.my_core.IllegalMoveError as e:
            print(e)
            j.append("FORFEIT")
    print("\nResults\n" + "%4s %4s %4s" % ("@", "o", "-"))
    print("-" * 15)
    print("%4i %4i %4i" % (j.count(BLACK), j.count(WHITE), j.count(TIE)))


if __name__ == "__main__":
    main()
