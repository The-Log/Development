def c2i(c, alphabet):
    return alphabet.index(c)

def i2c(i, alphabet):
    if i > len(alphabet):
        i = i - len(alphabet)
    return alphabet[i]

def prepare_string(s, alphabet):
    prepared = ""
    for i in list(s.upper()):
        if (i in alphabet):
            prepared = prepared + i
    return prepared
n
def vigenere_encode(plaintext, keyword, alphabet):
    """prepares plaintext and returns a new string shifted by shift, relative to alphabet"""

    plaintext = prepare_string(plaintext, alphabet)
    ciphertext = ''
    for i in range(len(plaintext)):
        li = c2i(plaintext[i], alphabet)
        kli = c2i(keyword[i % len(keyword)], alphabet)
        t = (li + kli) % 26
        ciphertext = ciphertext + i2c(t % len(alphabet), alphabet)
        
    return ciphertext


def vigenere_decode(ciphertext, keyword, alphabet):
    """return the plaintext, shifted by shift, relative to alphabet"""
    ciphertext = prepare_string(ciphertext, alphabet)
    plaintext = ''
    for i in range(len(ciphertext)):
        eli = c2i(ciphertext[i], alphabet)
        kli = c2i(keyword[i % len(keyword)], alphabet)
        t = (eli - kli)
        plaintext = plaintext + i2c(t % len(alphabet), alphabet)
    return plaintext

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext = "Secret message"
keyword = "WORD"
ciphertext = vigenere_encode(plaintext, keyword, alphabet)
print(ciphertext)
print(vigenere_decode(ciphertext, keyword, alphabet))
