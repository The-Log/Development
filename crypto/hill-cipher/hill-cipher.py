import numpy as np

def c2i(c, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Usage: c2i(c, alphabet). Returns the index of c in the string alphabet, starting at 0"""
    return alphabet.index(c)

def i2c(i, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Usage: i2c(i, alphabet). Returns the character at index i in alphabet"""
    return alphabet[i % len(alphabet)]

def prepare_string(s, alphabet):
    """Usage: prepare_string(s, alphabet). Removes characters from s not in alphabet, returns new string"""
    prepared = ""
    for i in list(s.upper()):
        if (i in alphabet):
            prepared = prepared + i
    return prepared

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

def hill_encode(plaintext, alphabet, m_b):
    plaintext = prepare_string(plaintext, alphabet)
    if len(plaintext) % 4 != 0:
        plaintext = plaintext + ('X' * (4 - len(plaintext) % 4))
    mod = len(alphabet)
    ciphertext = ""
    plaintext = list(plaintext)
    for i in range(0, len(plaintext) - 2, 4):
        m_a = [[c2i(plaintext[i], alphabet), c2i(plaintext[i+2], alphabet)],
               [c2i(plaintext[i+1], alphabet), c2i(plaintext[i+3], alphabet)]]
        #mi_b = matrix_inverse(m_b, mod)
        m_c = mat_mult(m_b, m_a, mod)
        ciphertext = ciphertext + i2c(m_c[0][0], alphabet) + i2c(m_c[1][0], alphabet) + i2c(m_c[0][1], alphabet) + i2c(m_c[1][1], alphabet)
    return ciphertext
        
def hill_decode(ciphertext, alphabet, m_b):
    ciphertext = prepare_string(ciphertext, alphabet)
    mod = len(alphabet)
    plaintext = ""
    ciphertext = list(ciphertext)
    for i in range(0, len(ciphertext) - 2, 4):
        m_a = [[c2i(ciphertext[i], alphabet), c2i(ciphertext[i+2], alphabet)],
               [c2i(ciphertext[i+1], alphabet), c2i(ciphertext[i+3], alphabet)]]
        mi_b = matrix_inverse(m_b, mod)
        m_c = mat_mult(mi_b, m_a, mod)
        plaintext = plaintext + i2c(m_c[0][0], alphabet) + i2c(m_c[1][0], alphabet) + i2c(m_c[0][1], alphabet) + i2c(m_c[1][1], alphabet)

    return plaintext

def get_same_digraphs(m_b, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    l = list()
    for i in list(alphabet):
        for j in list(alphabet):
            x = c2i(i)
            y = c2i(j)
            m_e = [[x,y]]
            m_f = mat_mult(m_e, m_d, 26)
            if m_f == m_e:
                l.append([[i2c(y1) for y1 in x1] for x1 in m_e])
    return l

def get_encoding(plaintext, ciphertext, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", di1='ab', di2='cd'):
    "determines the original encoding matrix or returns a matrix full of “-1”s if this is impossible."""
    crib = list(plaintext[:4])
    print(crib)
    d_crib = list(ciphertext[:4])
    c = [[c2i(crib[0]), c2i(crib[2])],[c2i(crib[1]), c2i(crib[3])]]
    d_c = [[c2i(d_crib[0]), c2i(d_crib[2])], [c2i(d_crib[1]), c2i(d_crib[3])]]
    print(c, d_c)
    mod = len(alphabet)
    m_i = matrix_inverse(c, mod)
    print(m_i)
    if m_i == -1:
        return [[-1 for j in i] for i in c]
    return mat_mult(d_c, m_i, mod)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plaintext = 'OLDY'#'FLEWIN'
ciphertext = 'JIFHSMBMSMTFSTWEPPWHJWOSULQE' #'GXIGBKYPCIGAKKRAUSFEVBGG' #

e_m = get_encoding(plaintext, ciphertext)
print(e_m)
b = hill_decode(ciphertext, alphabet, e_m)
print(b)
'''
m_b = [[4, 3], [5, 6]]
plaintext = "Lester S. Hill had a brilliant idea for a cipher"
ciphertext = "MVTHVEQHWAIKZRBIPGQTQBVEODDATWKFSVYR"
print(matrix_inverse(m_b, len(alphabet)))
a = hill_encode(plaintext, alphabet, m_b)
print(a)
b = hill_decode(a, alphabet, m_b)
print(b)

m_d = [[7, 6], [14, 3]]
print(get_same_digraphs(m_d))
'''
