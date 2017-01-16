import string
import numbers

alphabet = list(string.ascii_lowercase)
numofeach = [0] * 26

open_file = open("blocks.in", "r")
size = int(open_file.readline())

for w in open_file:
    w = w.rstrip("\n")
    temp = w.split()
    w1 = temp.pop()
    w2 = temp.pop()
    visited = set()
    for c in w1:
        numofeach[alphabet.index(c)] = numofeach[alphabet.index(c)] + 1
        visited.add(c)
    for c in w2:
        if(c not in visited):
            numofeach[alphabet.index(c)] = numofeach[alphabet.index(c)] + 1

out_file = open("blocks.out", "w")
for i in numofeach:
    print(i, file = out_file)
