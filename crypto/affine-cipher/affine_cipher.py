from math import gcd
from collections import Counter

def c2i(c, alphabet):
    """Usage: c2i(c, alphabet). Returns the index of c in the string alphabet, starting at 0"""
    return alphabet.index(c)

def i2c(i, alphabet):
    """Usage: i2c(i, alphabet). Returns the character at index i in alphabet"""
    return alphabet[i % len(alphabet)]

def d2i(d, alphabet):
    """Usage: d2i(d, alphabet). Returns the index of c in the string alphabet, starting at 0"""
    return c2i(d[0], alphabet) * len(alphabet) + c2i(d[1], alphabet)

def i2d(i, alphabet):
    """Usage: i2c(i, alphabet). Returns the character at index i in alphabet"""
    a = int(i / len(alphabet))
    b = i % len(alphabet)
    return alphabet[a] + alphabet[b]

def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    prepared = ""
    for i in list(s.upper()):
        if (i in alphabet):
            prepared = prepared + i
    return prepared

def mod_inverse(a, m):
    """finds the inverse of a mod m"""
    for i in range(0, m):
        if((a * i) % m == 1):
            return i
    return -1

def affine_encode(plaintext, alphabet, a, b):
    """encodes the given plaintext with the given alphabet using the given values of a and b"""
    m = len(alphabet)
    if gcd(a, m == 1):
        ciphertext = ""
        for c in list(plaintext):
            x = c2i(c, alphabet)
            y = (a * x + b) % m
            ciphertext = ciphertext + i2c(y, alphabet)
        return ciphertext
    else:
        return -1
def affine_decode(ciphertext, alphabet, a, b) :
    """find the inverse transformation for the given values of a and b and then decode the given ciphertext with the given alphabet."""
    plaintext = ""
    m = len(alphabet)
    for c in list(ciphertext):
        y = c2i(c, alphabet)
        x = (y - b) * (mod_inverse(a, m ** 2))
        plaintext = plaintext + i2c(x, alphabet)
    return plaintext

def affine_encode_digraphs(plaintext, alphabet, a, b):
    """encodes the given plaintext with the given alphabet using the given values of a and b"""
    m = len(alphabet)
    if len(plaintext) % 2 == 1:
        plaintext = plaintext + 'X'
    if gcd(a, m == 1):
        ciphertext = ""
        for i in range(0, len(plaintext), 2):
            d = plaintext[i: i + 2]
            x = d2i(d, alphabet)
            y = (a * x + b) % (m ** 2)
            ciphertext = ciphertext + i2d(y, alphabet)
        return ciphertext
    else:
        return -1

def affine_decode_digraphs(ciphertext, alphabet, a, b) :
    """find the inverse transformation for the given values of a and b and then decode the given ciphertext with the given alphabet."""
    plaintext = ""
    m = len(alphabet)
    for i in range(0, len(ciphertext), 2):
        d = ciphertext[i: i + 2]
        y = d2i(d, alphabet)
        x = (y - b) * (mod_inverse(a, m ** 2)) % m ** 2
        plaintext = plaintext + i2d(x, alphabet)
    return plaintext


def numb_transformations(size):
    x = 0
    for i in range(size):
        if (gcd(i, size) == 1):
            x = x + 1
    print(size, "\t" , x, "\t", size, "\t", x * size)

def get_ab(crib, ct, alphabet):
    mod = len(alphabet)
    m1 = c2i(crib[0], alphabet)
    m2 = c2i(crib[1], alphabet)
    f1 = c2i(ct[0], alphabet)
    f2 = c2i(ct[1], alphabet)
    return congru(m1, 1, f1, m2, 1, f2, mod)

def congru(a0,a1,a2, b0,b1,b2,c):
    for i in range(0,c):  
        for j in range(0,c): 
            if ((a0*i + a1*j) - a2)%c ==0 and ((b0*i +b1*j)-b2)%c==0:
                print('a: %d  b: %d' %( i, j))
                return i, j
            
alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ;:' #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(mod_inverse(13, 41 ** 2) % 41**2)
#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890abcde'
plaintext = 'I feel good and calm like a robot would!'
et = affine_encode_digraphs(plaintext, alphabet, 612, 280)
print(et)
ciphertext = ",ORwB,W,pbZOSugHG,jp!:egjA!YtuSOKnE:KwMw AP,!:egFe"
dt = affine_decode_digraphs(ciphertext, alphabet, 85, 1817)
print(dt)

#print(affine_decode('SWAP', alphabet, 25, 22))
#pt1 = 'EARLY'.upper()
#ct1 = 'SWAP'.upper()
#a, b = get_ab(pt1, ct1, alphabet)
#print(affine_decode(ct1, alphabet, a, b))

