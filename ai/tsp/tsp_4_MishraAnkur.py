import math
import random

class City:
   def __init__(self, x=None, y=None, name =None):
      self.x = None
      self.y = None
      self.name = None
      if x is not None:
         self.x = x
      else:
         self.x = int(random.random() * 200)
      if y is not None:
         self.y = y
      else:
         self.y = int(random.random() * 200)
      if name is not None:
         self.name = name
      else:
         self.y = "City" + str(int(random.random())*200)

   def get_x(self):
      return self.x

   def get_y(self):
      return self.y

   def dist(self, city):
       pi = math.pi
       y1  = self.get_y()
       x1  = self.get_x()
       y2  = city.get_y()
       x2  = city.get_x()
       R   = 3958.76
       y1 *= pi/180.0
       x1 *= pi/180.0
       y2 *= pi/180.0
       x2 *= pi/180.0
       if(y1 == y2 and x1 == x2):
           return 0
       return math.acos( math.sin(y1)*math.sin(y2) + math.cos(y1)*math.cos(y2)*math.cos(x2-x1) ) * R

   def __repr__(self):
    return self.name + ": (" + str(self.get_x()) + ", " + str(self.get_y()) + ")"

class TourManager:
   destinationCities = []

   def addCity(self, city):
      self.destinationCities.append(city)

   def get_city(self, index):
      return self.destinationCities[index]

   def tour_size(self):
      return len(self.destinationCities)

class Tour:
   def __init__(self, tourmanager, tour=None):
      self.tourmanager = tourmanager
      self.tour = []
      self.fitness = 0.0
      self.dist = 0
      if tour is not None:
         self.tour = tour
      else:
         for i in range(0, self.tourmanager.tour_size()):
            self.tour.append(None)

   def __len__(self):
      return len(self.tour)

   def __getitem__(self, index):
      return self.tour[index]

   def __setitem__(self, key, value):
      self.tour[key] = value

   def __repr__(self):
      geneString = "|"
      for i in range(0, self.ts()):
         geneString += str(self.get_city(i)) + "| "
      return geneString

   def generateIndividual(self):
      for cityIndex in range(0, self.tourmanager.tour_size()):
         self.set_city(cityIndex, self.tourmanager.get_city(cityIndex))
      random.shuffle(self.tour)

   def get_city(self, tpition):
      return self.tour[tpition]

   def set_city(self, tpition, city):
      self.tour[tpition] = city
      self.fitness = 0.0
      self.dist = 0

   def get_fit(self):
      if self.fitness == 0:
         self.fitness = 1/float(self.get_d())
      return self.fitness

   def get_d(self):
      if self.dist == 0:
         td = 0
         for cityIndex in range(0, self.ts()):
            fromCity = self.get_city(cityIndex)
            destinationCity = None
            if cityIndex+1 < self.ts():
               destinationCity = self.get_city(cityIndex+1)
            else:
               destinationCity = self.get_city(0)
            td += fromCity.dist(destinationCity)
         self.dist = td
      return self.dist

   def ts(self):
      return len(self.tour)

   def contians_city(self, city):
      return city in self.tour

class Population:
   def __init__(self, tourmanager, size_population, initialise):
      self.tours = []
      for i in range(0, size_population):
         self.tours.append(None)

      if initialise:
         for i in range(0, size_population):
            newTour = Tour(tourmanager)
            newTour.generateIndividual()
            self.save(i, newTour)

   def __setitem__(self, key, value):
      self.tours[key] = value

   def __getitem__(self, index):
      return self.tours[index]

   def save(self, index, tour):
      self.tours[index] = tour

   def get_tour(self, index):
      return self.tours[index]

   def get_fittest(self):
      fittest = self.tours[0]
      for i in range(0, self.size_population()):
         if fittest.get_fit() <= self.get_tour(i).get_fit():
            fittest = self.get_tour(i)
      return fittest

   def size_population(self):
      return len(self.tours)

class GA:
   def __init__(self, tourmanager):
      self.tourmanager = tourmanager
      self.mutationRate = 0.25
      self.tournamentSize = 5
      self.elitism = True

   def evolve(self, pop):
      newPopulation = Population(self.tourmanager, pop.size_population(), False)
      elitismOffset = 0
      if self.elitism:
         newPopulation.save(0, pop.get_fittest())
         elitismOffset = 1

      for i in range(elitismOffset, newPopulation.size_population()):
         parent1 = self.select(pop)
         parent2 = self.select(pop)
         child = self.crossover(parent1, parent2)
         newPopulation.save(i, child)

      for i in range(elitismOffset, newPopulation.size_population()):
         self.mutate(newPopulation.get_tour(i))

      return newPopulation

   def crossover(self, parent1, parent2):
      child = Tour(self.tourmanager)

      startPos = int(random.random() * parent1.ts())
      endPos = int(random.random() * parent1.ts())

      for i in range(0, child.ts()):
         if startPos < endPos and i > startPos and i < endPos:
            child.set_city(i, parent1.get_city(i))
         elif startPos > endPos:
            if not (i < startPos and i > endPos):
               child.set_city(i, parent1.get_city(i))

      for i in range(0, parent2.ts()):
         if not child.contians_city(parent2.get_city(i)):
            for j in range(0, child.ts()):
               if child.get_city(j) == None:
                  child.set_city(j, parent2.get_city(i))
                  break

      return child

   def mutate(self, tour):
      for tp1 in range(0, tour.ts()):
         if random.random() < self.mutationRate:
            tp2 = int(tour.ts() * random.random())

            city1 = tour.get_city(tp1)
            city2 = tour.get_city(tp2)

            tour.set_city(tp2, city1)
            tour.set_city(tp1, city2)

   def select(self, pop):
      tournament = Population(self.tourmanager, self.tournamentSize, False)
      for i in range(0, self.tournamentSize):
         randomId = int(random.random() * pop.size_population())
         tournament.save(i, pop.get_tour(randomId))
      fittest = tournament.get_fittest()
      return fittest

d = dict()
tourmanager = TourManager()

open_names = open("rrNodeCity.txt", "r")
for n in open_names:
    n = n.strip("\n")
    arr =  n.split(" ")
    idc = arr[0]
    name = arr[1]
    # print(str(idc) +":"+ str(name))
    d[idc] = name

# print(d)
open_names.close()
open_nodes = open("rrNodes.txt", "r")
for n in open_nodes:
    n = n.strip("\n")
    arr =  n.split(" ")
    idc = arr[0]
    y = float(arr[1])
    x = float(arr[2])
    if(idc in d):
        city = City(x, y, d[idc])
        tourmanager.addCity(city)
open_nodes.close()

pop = Population(tourmanager, 50, True)


print("Initial distance: " + str(pop.get_fittest().get_d()))
print("Intial solution:")
print(pop.get_fittest())
print("")
ga = GA(tourmanager)
pop = ga.evolve(pop)
for i in range(0, 100):
  pop = ga.evolve(pop)
print("Finished")
print("")
print("Final distance: " + str(pop.get_fittest().get_d()))
print("Final Solution:")
print(pop.get_fittest())
