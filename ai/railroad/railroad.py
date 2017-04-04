from math import pi , acos , sin , cos
import heapq
from time import time
import pickle

class graph():
    def __init__(self):
        self.ntc = dict()
        self.nte = dict()
        self.nt_city = dict()
        self.city_name = dict()
        open_names = open("rrNodeCity.txt", "r")
        for n in open_names:
            n = n.strip("\n")
            arr =  n.split(" ")
            name = arr[0]
            city = arr[1]
            self.nt_city[city] = name
        open_names.close()
        open_nodes = open("rrNodes.txt", "r")
        for n in open_nodes:
            n = n.strip("\n")
            arr =  n.split(" ")
            city = arr[0]
            y = arr[1]
            x = arr[2]
            self.ntc[city] = (y,x)
        open_nodes.close()
        open_edges = open("rrEdges.txt", "r")
        for n in open_edges:
            n = n.strip("\n")
            arr =  n.split(" ")
            city = arr[0]
            edge = arr[1]
            if(city in self.nte):
                self.nte[city][edge] = (self.dist(self.ntc[city][0], self.ntc[city][1], self.ntc[edge][0], self.ntc[edge][1]))
                if(edge in self.nte):
                    self.nte[edge][city] = (self.dist(self.ntc[city][0], self.ntc[city][1], self.ntc[edge][0], self.ntc[edge][1]))
                else:
                    self.nte[edge] = {city : self.dist(self.ntc[city][0], self.ntc[city][1], self.ntc[edge][0], self.ntc[edge][1])}
            else:
                self.nte[city] = {edge : self.dist(self.ntc[city][0], self.ntc[city][1], self.ntc[edge][0], self.ntc[edge][1])}
                if(edge in self.nte):
                    self.nte[edge][city] = (self.dist(self.ntc[city][0], self.ntc[city][1], self.ntc[edge][0], self.ntc[edge][1]))
                else:
                    self.nte[edge] = {city : self.dist(self.ntc[city][0], self.ntc[city][1], self.ntc[edge][0], self.ntc[edge][1])}

        open_edges.close()

    def edge_cost(self, state, c):
        return self.nte[state][c]

    def display(self):
        print(self.nte)

    def dist(self, y1, x1, y2, x2):
         y1  = float(y1)
         x1  = float(x1)
         y2  = float(y2)
         x2  = float(x2)
         R   = 3958.76
         y1 *= pi/180.0
         x1 *= pi/180.0
         y2 *= pi/180.0
         x2 *= pi/180.0
         if(y1 == y2 and x1 == x2):
             return 0
         return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

# G = graph()
# pickle.dump(G, open("graph.p", "wb"))

G = pickle.load(open("graph.p", "rb"))
class node():
    def __init__(self, parent = None, node = "1700665", goal = "1701128", edges = G.nte["1700665"], depth = 0):
        self.parent = parent
        self.goal = goal
        self.node = node
        self.depth = depth
        self.edges = edges
        self.lat = G.ntc[node][1]
        self.long = G.ntc[node][0]

        if(parent != None):
            self.g = G.edge_cost(parent.node, node) + parent.g
        else:
            self.g = 0
        self.h = heuristic(self, self.goal)
        self.f = self.h + self.g


    def expand(self):
        children = []
        childNames = []
        parent = self
        for e in self.edges:
            s = node(parent, e, self.goal, G.nte[e], self.depth + 1)
            children.append(s)
            childNames.append(s.node)
        return children

    def get_path(self):
        path = []
        while(self != None):
            path.append(self.node)
            self = self.parent
        path.reverse()
        return path

    def __lt__(self,other):
        return self.f < other.f

def heuristic(node, goal):
    return G.dist(node.long, node.long, G.ntc[goal][0], G.ntc[goal][1])

def search(start_node):
    frontier = []
    frontier.append(start_node)
    visited = set()
    while(True):
        if(len(frontier) == 0):
            return None
        current = heapq.heappop(frontier)
        if(current.node ==  current.goal):
            return current.g
        if(current.node not in visited):
            visited.add(current.node)
            for n in current.expand():
                heapq.heappush(frontier, n)

open_test = open("rrTest.txt", "r")
write_solutions = open("solutions.txt", "w")
for n in open_test:
    n = n.strip("\n")
    arr =  n.split(", ")
    start = arr[0]
    end = arr[1]
    sn = node(None, G.nt_city[start], G.nt_city[end], G.nte[G.nt_city[start]], 0)
    start_time = time()
    searchDist = search(sn)
    end_time = time()
    print(start + "\t\t\t" + end+ "\t\t\t" + str(searchDist) + "\t\t\t" +str(end_time - start_time) + "\n")
    write_solutions.write(start + "\t\t\t" + end+ "\t\t\t" + str(searchDist) + "\t\t\t" +str(end_time - start_time) + "\n")
open_test.close()
write_solutions.close()
