from collections import Counter

def prepare_string(s, alphabet):
    prepared = ""
    for i in list(s.upper()):
        if (i in alphabet):
            prepared = prepared + i
    return prepared

def frequent_letters(text, alphabet):
    text = prepare_string(text, alphabet)
    bigraphs = []
    for index in range(len(text) - 1):
        bigraphs.append(text[index:index + 1])
    c = Counter(bigraphs)
    return c.most_common(4)
    """ return a list of tuples of most common letters in 'text'"""

def frequent_bigraphs(text, alphabet):
    """ return a list of tuples of most common bigraphs in 'text'"""
    text = prepare_string(text, alphabet)
    bigraphs = []
    for index in range(len(text) - 1):
        bigraphs.append(text[index:index + 2])
    c = Counter(bigraphs)
    return c.most_common(4) # Feel free to change this number.

def frequent_trigraphs(text, alphabet):
    """ return a list of tuples of most common trigraphs in 'text'"""
    #text = prepare_string(text, alphabet)
    bigraphs = []
    for index in range(len(text) - 1):
        if ' ' not in text[index:index + 3]:
            bigraphs.append(text[index:index + 3])
    c = Counter(bigraphs)
    return c.most_common(4)

def frequent_double_letters(text, alphabet):
    """ return a list of tuples of most common double letters in 'text'"""
    text = prepare_string(text, alphabet)
    bigraphs = []
    for index in range(len(text) - 1):
        if text[index:index+1] == text[index+1:index+2]:
            bigraphs.append(text[index:index + 2])
    c = Counter(bigraphs)
    return c.most_common(4)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = 'ZFNNANWJWYBZLKEHBZTNSKDDGJWYLWSBFNSSJWYFNKBGLKOCNKSJEBDWZFNGKLJKJNQFJPFJBXHBZTNRDKNZFNPDEJWYDRPDEGCNZNWJYFZZFLZTCNBBNBZFNNLKZFSLKONWBLCCKJANKBPHGBZFNGNLOBLWSRDCSBZFNRJWLCBFDKNJWLWSWDTDSUWDTDSUOWDQBQFLZBYDJWYZDFLGGNWZDLWUTDSUTNBJSNBZFNRDKCDKWKLYBDRYKDQJWYDCSJZFJWODRSNLWEDKJLKZUJNANWZFJWODRDCSSNLWEDKJLKZUZFNRLZFNKQNWNANKRDHWSJZFJWODRSNLWEDKJLKZU'
print("Ciphertext = %s" % ciphertext)

ct1 = ciphertext.lower()
print('')

fl = frequent_letters(ciphertext, alphabet)
print(fl)
print(frequent_trigraphs(ciphertext, alphabet))

print('')
ct1 = ct1.replace('zfn', 'THE ')

ct1 = ct1.replace('z', 'T')
ct1 = ct1.replace('f', 'H')
ct1 = ct1.replace('n', 'E')

ct1 = ct1.replace('a', 'V')

ct1 = ct1.replace('j', 'I')
ct1 = ct1.replace('w', 'N')
ct1 = ct1.replace('y', 'G')


plaintext = ct1 
print('plaintext = ', plaintext)
print("")

'''
Exercise 2.

AJM PQMCIY QVJ, XJR HCYBQ TNGG QBCP N OCQ BNMS.  NP CQ QRMIP JRQ, C TNI YJ N GJIY VNX VCQBJRQ RPCIY NIX JA QBNQ QBCIY KJPQS AMJH JRM RPRNG GNXJRQ NQ NGG.

ct1 = ct1.replace('p', 'S')
ct1 = ct1.replace('n', 'A')
ct1 = ct1.replace('b', 'H')
ct1 = ct1.replace('q', 'T')
ct1 = ct1.replace('c', 'I')
ct1 = ct1.replace('i', 'N')
ct1 = ct1.replace('g' , 'L')
ct1 = ct1.replace('j' , 'O')
ct1  = ct1.replace('m', "R")
ct1  = ct1.replace('a', "F")
ct1  = ct1.replace('y', "G")
ct1  = ct1.replace('s', "D")
ct1  = ct1.replace('o', "B")
ct1  = ct1.replace('v', "W")
ct1  = ct1.replace('r', "U")
ct1  = ct1.replace('t', "C")
ct1  = ct1.replace('x', "Y")
ct1  = ct1.replace('h', "M")

Exercise 4.

ANUYJKHNFL JLNBL, NBENJK YNK KHNKIONS: \'JNYNHYJ - SNJKONS, INHKONS, JNHDSNJ ONBRNJ!\'

ct1 = ct1.replace('o', 'F')
ct1 = ct1.replace('n', 'U')
ct1 = ct1.replace('s', 'L')
ct1 = ct1.replace('j', 'S')
ct1 = ct1.replace('k', 'T')
ct1 = ct1.replace('h', 'R')
ct1 = ct1.replace('l', 'K')
ct1 = ct1.replace('b', 'N')
ct1 = ct1.replace('i', 'H')
ct1 = ct1.replace('y', 'B')
ct1 = ct1.replace('d', 'P')
ct1 = ct1.replace('r', 'G')
ct1 = ct1.replace('e', 'J')
ct1 = ct1.replace('a', 'D')
ct1 = ct1.replace('u', 'M')
ct1 = ct1.replace('f', 'C')
'''

