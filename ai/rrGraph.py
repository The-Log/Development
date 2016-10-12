from math import pi , acos , sin , cos
import pickle

class graph():
    def __init__(self):
        self.name_to_cord = dict()
        self.name_to_edge = dict()
        open_nodes = open("rrNodes.txt", "r")
        for n in open_nodes:
            n = n.strip("\n")
            arr =  n.split(" ")
            city = arr[0]
            y = arr[1]
            x = arr[2]
            self.name_to_cord[city] = (y,x)
        open_nodes.close()
        open_edges = open("rrEdges.txt", "r")
        for n in open_edges:
            n = n.strip("\n")
            arr =  n.split(" ")
            city = arr[0]
            edge = arr[1]
            if(city in self.name_to_edge):
                self.name_to_edge[city][edge] = (self.dist(self.name_to_cord[city][0], self.name_to_cord[city][1], self.name_to_cord[edge][0], self.name_to_cord[edge][1]))
                if(edge in self.name_to_edge):
                    self.name_to_edge[edge][city] = (self.dist(self.name_to_cord[city][0], self.name_to_cord[city][1], self.name_to_cord[edge][0], self.name_to_cord[edge][1]))
                else:
                    self.name_to_edge[edge] = {city : self.dist(self.name_to_cord[city][0], self.name_to_cord[city][1], self.name_to_cord[edge][0], self.name_to_cord[edge][1])}
            else:
                self.name_to_edge[edge] = {city : self.dist(self.name_to_cord[city][0], self.name_to_cord[city][1], self.name_to_cord[edge][0], self.name_to_cord[edge][1])}
                self.name_to_edge[city] = {edge : self.dist(self.name_to_cord[city][0], self.name_to_cord[city][1], self.name_to_cord[edge][0], self.name_to_cord[edge][1])}
        open_edges.close()
    def edge_cost(self, state, c):
        return self[state][c]
    def heuristic(self, node, goal):
        return 1
    def display(self):
        print(self.name_to_edge)

    def dist(self, y1,x1, y2,x2):
         y1  = float(y1)
         x1  = float(x1)
         y2  = float(y2)
         x2  = float(x2)
         R   = 3958.76
         y1 *= pi/180.0
         x1 *= pi/180.0
         y2 *= pi/180.0
         x2 *= pi/180.0
         return acos( min(1, sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1)) ) * R


G = graph()
visited = set()
dict1 = G.name_to_edge
pickle.dump(G, open("graph.p", "wb"))

class node():
    def __init__(self, parent = None, start = "1700665", goal = "1701128", edges = G["1700665"], depth = 0, cost = 0):
        self.parent = parent
        self.goal = goal
        self.start = start
        self.depth = depth
        self.edges = edges
        self.cost = cost

    def expand(self):
        children = []
        parent = self
        for e in self.edges:
            if(e not in visited):
                s = node(parent, e, self.goal, G[e], self.depth + 1, self.g + edge_cost() + heuristic())
                children.append(s)
                visited.add(e)
        return children

    def get_path(self):
        path = []
        while(self != None):
            path.append(self)
            self = self.parent
        path.reverse()
        return path

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
