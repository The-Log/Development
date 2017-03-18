import pickle

#noun2ids = dict()
#id2synset = dict()
noun2ids = pickle.load( open( "noun2ids.p", "rb" ) )
id2synset = pickle.load( open( "id2synset.p", "rb" ) )

class wordNet:
    def __init__(self, synsets, hypernyms):
        pass

    def read_synsets(self, sysnets):
        if len(noun2ids) != 0 and len(id2synset) != 0:
            print("succ my wewe")
            return
        print("I luv large dongers")
        open_file = open(sysnets, "r")
        for w in open_file:
            w = w.rstrip("\n")
            tokens = w.split(",")
            idnum = int(tokens.pop(0))
            nouns = tokens.pop(0)
            id2synset[idnum] = nouns
            #print(str(idnum) + id2synset[idnum])
            nouns = nouns.split(" ")
        open_file.close()

    def read_hypernyms(self, hypernyms):
        if len(noun2ids) != 0 and len(id2synset) != 0:
            print("succ my wewe")
            return
        print("I luv large dongers")
        open_file = open(sysnets, "r")
        for w in open_file:
            w = w.rstrip("\n")
            tokens = w.split(",")
            idnum = int(tokens.pop(0))
            nouns = tokens.pop(0)
            id2synset[idnum] = nouns
            #print(str(idnum) + id2synset[idnum])
            nouns = nouns.split(" ")
        open_file.close()


    def nouns(self):
        return noun2ids

    def is_noun(self, word):
        return world in noun2ids

    def sca(noun1, noun2):
        pass

    def verify(noun):
        if self.is_noun(noun) == False:
            raise ValueError("Not a noun!")
    def distance(noun1, noun2):
        pass

wn = wordNet("synsets.txt", "hypernyms.txt")
wn.read_sysnets("synsets.txt")

print(noun2ids["a"])

pickle.dump(noun2ids, open("noun2ids.p", "wb"))
pickle.dump(id2synset, open("id2synset.p", "wb"))
