import string
import heapq
from collections import deque
from time import time

st = time()

open_file = open("words_06.txt", "r")
dictionary = set()

for w in open_file:
    w = w.rstrip("\n")
    dictionary.add(w)
open_file.close()
visited = set()
alphabet = list(string.ascii_lowercase)

start = raw_input("Give me a six letter word! ")
end = raw_input("Another six letter word! ")

class node():
    def __init__(self, parent = None, word = "Garden", goal="easier", depth = 0):
        self.parent = parent
        self.goal = goal
        self.word = word.lower()
        self.depth = depth
        self.cost = 0
        for i in range(len(word)):
            if self.word[i] != self.goal[i]:
                self.cost = self.cost + 1

    def get_children(self):
        children = []
        parent = self
        for i in range(len(self.word)):
            s = list(self.word)
            for j in range(len(alphabet)):
                s[i] = alphabet[j]
                w = "".join(s)
                if(w in dictionary and w not in visited):
                    visited.add(w)
                    children.append(node(parent, w, self.goal, self.depth + 1 ))
        return children

    def get_path(self):
        path = []
        while(self != None):
            path.append(self)
            self = self.parent
        path.reverse()
        return path

    def __str__(self):
        return str(self.word)

    def __lt__(self,other):
        return self.cost < other.cost

def search(start_node):
    frontier = []
    frontier.append(start_node)
    while(True):
        if(len(frontier) == 0):
            return None
        current = heapq.heappop(frontier)
        if(str(current) ==  end.lower()):
            return current.get_path()
        lA = current.get_children()
        frontier.extend(lA)
        heapq.heapify(frontier)


start_node = node(None, start, end, 0)
start = time()
listA = search(start_node)
end = time()

print("Path: ")
for i in listA:
    print(i)
print("")
print("It took " + str(len(listA)) + " steps")
print("Time it took: " + str(end - start))
