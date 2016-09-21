class minHeap:
    def __init__(self, size):
        self.size = size
        self.mh = [0] * (size + 1)
        self.pos = 0
    def make_heap(self, listA):
        if len(listA) > 0 :
            for i in range(len(listA)):
                self.insert(listA[i])
    def insert(self, x):
        if(self.pos == 0):
            self.mh[self.pos + 1] = x
            self.pos = 2
        else:
            self.mh[self.pos] = x
            self.pos = self.pos + 1
            self.bubble_up()

    def bubble_up(self):
        pos = self.pos - 1
        while(pos > 0 and self.mh[pos / 2] > self.mh[pos]):
            y = self.mh[pos]
            self.mh[pos] = self.mh[pos / 2]
            self.mh[pos / 2] = y
            pos =  pos / 2
    def extract_min(self):
        minimum = self.mh[1]
        self.mh[1] = self.mh[self.pos - 1]
        self.mh[self.pos-1] = 0
        self.pos = self.pos - 1
        self.sink_down(1)
        return minimum
    def sink_down(self, k):
        a = self.mh[k]
        smallest =  k
        if(2*k < self.pos and self.mh[smallest] > self.mh[2*k]):
            smallest =  2*k
        if 2*k + 1 < self.pos and self.mh[smallest] > self.mh[2*k+1]:
            smallest = 2*k+1
        if smallest != k:
            self.swap(k,smallest)
            self.sink_down(smallest)
    def swap(self, a, b):
        temp = self.mh[a]
        self.mh[a] = self.mh[b]
        self.mh[b] = temp
    def display(self):
        for i in range(1,self.size):
            print(self.mh[i])
listA =  [3,2,1,7,8,4,10,16,12]
print("Orignal: ")
for i in range(len(listA)):
    print(listA[i])
m = minHeap(len(listA))
print("New: ")
m.make_heap(listA)
m.display()
for i in range(len(listA)):
    print(m.extract_min())
