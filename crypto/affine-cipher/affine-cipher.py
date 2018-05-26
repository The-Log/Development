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


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890abcde'
ciphertext = "QFHIIRTBUUYNNUURJPXDYWFG"
plaintext = affine_decode_digraphs(ciphertext, alphabet, 81, 119)
print(numb_transformations(26))
