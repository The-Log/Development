import numpy as np
from PIL import Image
from math import gcd

def mod_inverse(a, m):
    """Usage: mod_inverse(a, m).finds the inverse of a mod m"""
    for i in range(0, m):
        if((a * i) % m == 1):
            return i
    return -1

def matrix_inverse(mat, mod):
    d = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0] 
    d_inverse = mod_inverse(d, mod)
    if (d_inverse == -1):
        return -1
    lel = [[mat[1][1], -mat[0][1]], [-mat[1][0], mat[0][0]]]
    mat_inverse = [[j * d_inverse for j in i] for i in lel]
    mod_mat_inverse = [[j % mod for j in i] for i in mat_inverse]
    return mod_mat_inverse

def mat_mult(m_a, m_b, mod):
    lel = (np.matrix(m_a) * np.matrix(m_b)).tolist()
    return [[j % mod for j in i] for i in lel]


def caesar_shift(im, shift):
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            im.putpixel((i, j), (im.getpixel((i, j)) + shift) % 256)
    return im

def hill_encode(im, m_b, v = None):
    mod = 256
    switch = 0
    for i in range(im.size[1]):
        for j in range (0,  im.size[0], 2):
           
           m_a = [[im.getpixel((j, i))], [im.getpixel((j + 1, i))]]
           
           m_c = mat_mult(m_b, m_a, mod)
           im.putpixel((j, i), m_c[0][0] % 256)
           im.putpixel((j + 1, i), m_c[1][0] % 256)
           if switch == 0 and v is not None:
               m_b[0][0] = m_b[0][0] * v[0] % mod
               m_b[0][1] = m_b[0][1] * v[1] % mod
               switch = 1
           else:
               if (v is not None):
                   m_b[1][0] = m_b[1][0] * v[0] % mod
                   m_b[1][1] = m_b[1][1] * v[1] % mod
                   switch = 0
           
    return im

def hill_decode(im, m_b, v = None):
    mod = 256
    switch = 0

    for i in range(im.size[1]):
        for j in range (0,  im.size[0], 2):

           m_a = [[im.getpixel((j, i))], [im.getpixel((j + 1, i))]]

            
           mi_b = matrix_inverse(m_b, mod)
           m_c = mat_mult(mi_b, m_a, mod)
           im.putpixel((j, i), m_c[0][0] % 256)
           im.putpixel((j+1, i), m_c[1][0] % 256)
           if switch == 0 and v is not None:
               m_b[0][0] = m_b[0][0] * v[0] % mod
               m_b[0][1] = m_b[0][1] * v[1] % mod
               switch = 1
           else:
               if (v is not None):
                   m_b[1][0] = m_b[1][0] * v[0] % mod
                   m_b[1][1] = m_b[1][1] * v[1] % mod
                   switch = 0
      
    return im

def affine_encode(im, a, b):
    """encodes the given plaintext with the given alphabet using the given values of a and b"""
    m = 256
    if gcd(a, m == 1):
        ciphertext = ""
        
        for i in range(im.size[1]):
            for j in range (0,  im.size[0]):
                x = im.getpixel((j, i))
                y = (a * x + b) % m
                im.putpixel((j, i), y)
        return im
    else:
        return -1

def affine_decode(im, a, b) :
    """find the inverse transformation for the given values of a and b and then decode the given ciphertext with the given alphabet."""
    m = 256
    for i in range(im.size[1]):
            for j in range (0,  im.size[0]):
                y = im.getpixel((j, i))
                x = (y - b) * (mod_inverse(a, m ** 2))
                im.putpixel((j, i), x)
    return im
    
filename = 'SC.bmp'
im = Image.open('images/' + filename).convert("L")  

'''
caesar_shift(im, 53)
im.show()
im.save('encoded/caesar-' + filename)
'''

im.show()
v = [101, 141]
m_b = [[2, 5], [3, 20]]

hill_encode(im, m_b, v)
affine_encode(im, 81, 119)
#hill_encode(im, m_b, v)
#caesar_shift(im, 53)

im.show()
im.save('encoded/encoded-vector-' + filename)

#caesar_shift(im, -53)
affine_decode(im, 81, 119)
hill_decode(im, m_b, v)
#hill_decode(im, m_b, v)

im.show()
#im.save('decoded/decoded-' + filename)

