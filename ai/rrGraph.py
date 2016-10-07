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
         return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

G = graph()
dict1 = G.name_to_edge
print(dict1["4200421"]["4200412"])
pickle.dump(G, open("graph.p", "wb"))
