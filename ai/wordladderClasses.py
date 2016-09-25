import string
from collections import deque
from time import time
st = time()

open_file = open("words.txt", "r")
dictionary = []

for w in open_file:
    w = w.rstrip("\n")
    dictionary.append(w)
open_file.close()

visited = set()
alphabet = list(string.ascii_lowercase)

start = 'Garden' #raw_input("Give me a six letter word! ")
end = 'easier'   #raw_input("Another six letter word! ")

class node():
    def __init__(self, parent = None, word = "Garden", depth = 0, cost=0 ):
        self.parent = parent
        self.word = word.lower()
        self.depth = depth
        self.cost = cost
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
                    children.append(node(parent, w, self.depth + 1))
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


def search(start_node):
    frontier = deque()
    frontier.append(start_node)
    while(True):
        if(len(frontier) == 0):
            return None
        current = frontier.popleft()
        if(str(current) ==  end.lower()):
            return current.get_path()
        lA = current.get_children()
        frontier.extend(lA)

start_node = node(None, start, 0, 0)
listA = search(start_node)

print("Path: ")
for i in listA:
    print(i)
print("")
print("Time it took: " + str(time() - st))
