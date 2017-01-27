import os, signal
import time
import strategy as ai
from multiprocessing import Process, Value
time_limit = 5

def best_strategy(player, board, best_move, still_running):
	while(still_running.value > 0 and best_move.value<1000):
		time.sleep(1)
		best_move.value += 100

def get_move():
	best_move = Value("i",0)
	running = Value("i",1)
	p = Process(target=best_strategy, args=("", "",  best_move, running)) # create a sub process
	p.start()	# start it
	t1 = time.time()
	move = best_move.value	# get the final best move

    return move
if __name__=="__main__":
	get_move()
