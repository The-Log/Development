from collections import deque
from heapq import heappush, heappop
from string import ascii_uppercase
from random import randint, sample
from pprint import pprint


G = {'A': ['B', 'F', 'C', 'G'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C', 'Z'],
     'E': ['F'],
     'F': ['C', 'Z'],
     'G': [],
     'Z': []}




def make_children(max_edges, nodes, max_weight=10):
    num_children = randint(0, max_edges)
    w = [randint(0, max_weight) for _ in range(max_edges)]
    c = sample(nodes, num_children)
    return c

def make_weights(G, max_weight=10):
    return {node:[randint(1,max_weight) for _ in children]
            for (node,children) in G.iteritems()}

nodes = ascii_uppercase[:10]

def make_graph(num_nodes, max_edges):
    nodes = set(ascii_uppercase[:num_nodes])
    return {n: make_children(max_edges, nodes) for n in nodes}

G = make_graph(22,4)
W = make_weights(G)

def pretty_path(tuple_path):
    path_list = []
    while(isinstance(tuple_path, tuple)):
        (prev_path, curr) = tuple_path
        path_list.append(curr)
        tuple_path = prev_path
    return path_list[::-1]


def tree_search(frontier, explore, add):
    def search(start, end, G):
        visited = set()
        add(frontier, [(None, start)])
        while(len(frontier) > 0):
            path = (_, current) = explore(frontier)
            visited.add(current)
            if current == end:
                return pretty_path(path)
            children = G[current]
            unvisited = [c for c in children if c not in visited]
            child_paths = [(path, c) for c in unvisited]
            add(frontier, child_paths)
        return None
    return search

def weighted_search(frontier, explore, add):
    def search(start, end, G, W):
        visited = set()
        add(frontier, [(0,(None, start))])
        while(len(frontier) > 0):
            cost, path = explore(frontier)
            _, current = path
            print cost, path
            visited.add(current)
            if current == end:
                return pretty_path(path)
            children = G[current]
            unvisited = [c for c in children if c not in visited]
            weighted = zip(W[current], children)
            child_paths = [(cost+w,(path, c)) for (w,c) in weighted]
            add(frontier, child_paths)
        return None
    return search

DFS = tree_search([], lambda frontier: frontier.pop(),
                  lambda frontier, to_add: frontier.extend(to_add))

BFS = tree_search(deque(), lambda frontier: frontier.popleft(),
                  lambda frontier, to_add: frontier.extend(to_add))

def heap_extend(heap, nodes):
    for node in nodes:
        heappush(heap, node)

DJK = weighted_search([], heappop, heap_extend)
print DJK('A', "L", G, W)
print BFS('A', 'L', G)
print DFS('A', 'L', G)

G = {'A': ['B', 'F', 'C', 'G'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C', 'Z'],
     'E': ['F'],
     'F': ['C', 'Z'],
     'G': [],
     'Z': []}
