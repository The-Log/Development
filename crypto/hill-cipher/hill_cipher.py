import numpy as np

def c2i(c, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Usage: c2i(c, alphabet). Returns the index of c in the string alphabet, starting at 0"""
    try:
        return alphabet.index(c)
    except ValueError:
        print(c)
        return -1
def i2c(i, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Usage: i2c(i, alphabet). Returns the character at index i in alphabet"""
    return alphabet[i % len(alphabet)]

def prepare_string(s, alphabet):
    """Usage: prepare_string(s, alphabet). Removes characters from s not in alphabet, returns new string"""
    prepared = ""
    for i in list(s):
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
        return [[-1, -1], [-1, -1]]
    lel = [[mat[1][1], -mat[0][1]], [-mat[1][0], mat[0][0]]]
    mat_inverse = [[j * d_inverse for j in i] for i in lel]
    mod_mat_inverse = [[j % mod for j in i] for i in mat_inverse]
    return mod_mat_inverse

def mat_mult(m_a, m_b, mod):
    lel = (np.matrix(m_a) * np.matrix(m_b)).tolist()
    return [[j % mod for j in i] for i in lel]
    
    
def hill_encode(plaintext, m_b, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
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
        
def hill_decode(ciphertext, m_b, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    ciphertext = prepare_string(ciphertext, alphabet)
    length = len(ciphertext)
    if len(ciphertext) % 4 != 0:
        ciphertext = ciphertext + ('X' * (4 - len(ciphertext) % 4))
    mod = len(alphabet)
    plaintext = ""
    ciphertext = list(ciphertext)
    for i in range(0, len(ciphertext) - 2, 4):
        m_a = [[c2i(ciphertext[i], alphabet), c2i(ciphertext[i+2], alphabet)],
               [c2i(ciphertext[i+1], alphabet), c2i(ciphertext[i+3], alphabet)]]
        mi_b = matrix_inverse(m_b, mod)
        m_c = mat_mult(mi_b, m_a, mod)
        plaintext = plaintext + i2c(m_c[0][0], alphabet) + i2c(m_c[1][0], alphabet) + i2c(m_c[0][1], alphabet) + i2c(m_c[1][1], alphabet)

    return plaintext[:length]

def get_same_digraphs(m_b, alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
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

alphabet = "".join(chr(x) for x in range(33,94))

def get_encoding(plaintext, ciphertext, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", di1='ab', di2='cd'):
    "determines the original encoding matrix or returns a matrix full of “-1”s if this is impossible."""
    crib = list(plaintext[:4])
    #print(crib)
    d_crib = list(ciphertext[:4])
    c = [[c2i(crib[0], alphabet), c2i(crib[2], alphabet)],[c2i(crib[1], alphabet), c2i(crib[3], alphabet)]]
    d_c = [[c2i(d_crib[0], alphabet), c2i(d_crib[2], alphabet)], [c2i(d_crib[1], alphabet), c2i(d_crib[3], alphabet)]]
    #print(c, d_c)
    mod = len(alphabet)
    m_i = matrix_inverse(c, mod)
    #print(m_i)
    
    return mat_mult(d_c, m_i, mod)

def get_bruteforce(plaintext_block, ciphertext_block, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", mod=26):
    functional = []
    ct = ciphertext_block
    pt = plaintext_block
    c_matrix = [[c2i(ct[0], alphabet), c2i(ct[2], alphabet)], [c2i(ct[1], alphabet), c2i(ct[3], alphabet)]]
    p_matrix = [[c2i(pt[0], alphabet), c2i(pt[2], alphabet)], [c2i(pt[1], alphabet), c2i(pt[3], alphabet)]]
    #print(c_matrix)
    #print(p_matrix)
    for i in range(mod):
        for j in range(mod):
            for k in range(mod):
                for l in range(mod):
                    enc_mat = [[i,j],[k,l]]
                    dec_mat = matrix_inverse(enc_mat, mod)
                    if dec_mat == -1:
                        continue
                    if mat_mult(enc_mat, p_matrix, mod) == c_matrix:
                        functional.append(enc_mat)
    print("Found %d functional enc matrices!" % len(functional))
    return functional

if __name__ == '__main__':
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.!?, ;:'
    plaintext = 'I feel like a...contradiction!'
    m_b = [[32, 12], [1, 14]]
    print(hill_encode(plaintext, m_b, alphabet))
    m_c = [[15, 7], [3,36]]
    ct = 'V:gJknRJ:ckNMJlLSgiso,KWQq??,kR .T'
    print(hill_decode(ct, m_c, alphabet))

    
    ct1 = 'V:,VMCmwmpuE.ZRJ,sPX;IJK?ttvnpJqECHoqeUfsmzxNqldAiHoF,UQNvTLBUECnpmp.:MqDzpWuEpKkNMJRJ,sPX;IQq;Iin'
    crib = 'I dreamed'
    l = get_encoding(crib, ct1, alphabet)
    print(hill_decode(ct1, l, alphabet))
    poss = get_bruteforce(crib, ct1, alphabet, len(alphabet))
    
    '''
    print(mod_inverse(9, 26))
    ct = 'GXIGBKYPCIGAKKRAUSFEVBGG'
    crib = 'FLEWIN'
    poss = get_bruteforce(crib, ct)
    print(poss)
    m_b = poss[0]
    pt = hill_decode(ct, m_b)
    print(pt)
    #print(len(ct) == len(pt))
    '''
