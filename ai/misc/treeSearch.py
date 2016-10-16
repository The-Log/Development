
from collections import deque

class Stack(object):
    def __init__(self):
        self._stack = []
    def add(self, nodes):
        for node in nodes:
            self._stack.append(node)
    def explore(self):
        return self._stack.pop()
    def is_empty(self):
        return (len(self._stack) == 0)

class Queue(object):
    def __init__(self):
        self._queue = deque()
    def add(self, nodes):
        for node in nodes:
            self._queue.append(node)
    def explore(self):
        return self._queue.popleft()
    def is_empty(self):
        return (len(self._queue) == 0)

class Frontier(object):
    def __init__(self, nodes_struct, explore):
        self.struct = nodes_struct
        self.add = lambda nodes: [self.struct.append(node) for node in nodes]
        self.is_empty = lambda: len(self.struct) == 0
        self.explore_fn = explore
    def explore(self):
        return self.explore_fn(self.struct)

DFS = lambda : Frontier([], lambda struct: struct.pop())
BFS = lambda : Frontier(deque(), lambda struct: struct.popleft())

class Path(object):
    def __init__(self, node, prev=None):
        self.previous = prev
        self.node = node
    def __repr__(self):
        out = ' '
        current = self
        reversed_path = []
        while current is not None:
            reversed_path.append(current.node)
            current = current.previous
        return out.join(reversed_path[::-1])

def tree_search(start, goal, G, frontier = Queue()):
    visted = set()
    frontier.add([Path(start)])
    while not frontier.is_empty():
        current = frontier.explore()
        if current.node == goal:
            return current
        visted.add(current.node)
        children = G[current.node]
        unvisited = [c for c in children if c not in visted]
        paths = [Path(u, current) for u in unvisited]
        frontier.add(paths)
    return 'None'


G = {'A': ['B', 'C',"E"],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']}
print tree_search('A', 'D', G, Queue())
print tree_search('A', 'D', G, DFS())
