import re

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

def caesar_shift_encode(plaintext, shift, alphabet):
    """prepares plaintext and returns a new string shifted by shift, relative to alphabet"""

    plaintext = prepare_string(plaintext, alphabet)
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext = ciphertext + i2c(c2i(plaintext[i], alphabet) + shift, alphabet)
    return ciphertext

def caesar_shift_decode(ciphertext, shift, alphabet):
    """return the plaintext, shifted by shift, relative to alphabet"""
    ciphertext = prepare_string(ciphertext, alphabet)
    plaintext = ''
    for i in range(len(ciphertext)):
        plaintext = plaintext  + i2c(c2i(ciphertext[i], alphabet) - shift, alphabet)
    return plaintext

def subst_validate(alpha1, alpha2):
    """verify that alpha1 and alpha2 contain exactly the same letters, return boolean"""
    if sorted(alpha1) == sorted(alpha2):
        return True
    return False


def substitution_cipher_encode(plaintext, alpha1, alpha2):
    """prepares plaintext, validates the alphabets, and returns a ciphertext using alpha2 as the substitution cipher alphabet"""
    prepared = prepare_string(plaintext, alpha1)
    ciphertext = ""
    if subst_validate(alpha1, alpha2):
        for c in list(prepared):
            ciphertext = ciphertext + i2c(c2i(c, alpha1), alpha2)
        return ciphertext
    return "Error!"

def substitution_cipher_decode(ciphertext, alpha1, alpha2):
    """prepares plaintext, validates the alphabets, and returns a plaintext using alpha1 as the original alphabet"""
    plaintext = ''
    if subst_validate(alpha1, alpha2):
        for c in list(ciphertext):
            plaintext = plaintext + i2c(c2i(c, alpha2), alpha1)
        return plaintext
    return "Error!"

def make_cipher_alphabet(alphabet, keyword):
    """creates a cipher alphabet using the given keyword and returns it"""
    s = set()
    l = []
    for i in list(keyword + alphabet):
        if i not in s:
            l.append(i)
            s.add(i)
    return ''.join(l)          

def keyword_substitution_cipher_encode(plaintext, keyword, alphabet_source):
    """ return a string encoding plaintext using a keyword subst. cipher with 'keyword'
    as the keyword and 'alphabet_source' as the source alphabet. """
    alpha2 = make_cipher_alphabet(alphabet_source, keyword)
    print(alpha2)
    return substitution_cipher_encode(plaintext, alphabet_source, alpha2)

def keyword_substitution_cipher_decode(ciphertext, keyword, alphabet_source):
    """ return a string decoding ciphertext using a keyword subst. cipher with 'keyword'
     as the keyword and 'alphabet_source' as the source alphabet. """
    alpha2 = make_cipher_alphabet(alphabet_source, keyword)
    return substitution_cipher_decode(ciphertext, alphabet_source, alpha2)


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




print("\n---Testing Keyword Substitution-------")
plaintext = "To be or not to be, that is the question"
keyword = "SHAKESPEARE"
print("Cipher alphabet is " + make_cipher_alphabet(alphabet, keyword))
ciphertext = keyword_substitution_cipher_encode(plaintext, keyword, alphabet)
recovered_text = keyword_substitution_cipher_decode(ciphertext, keyword, alphabet)
print("\n---Frequency of Letters-------")
text = 'Goldfishes are good and dank'
print("Bigraphs", frequent_bigraphs(text, alphabet))
print("Trigraphs", frequent_trigraphs(text , alphabet))
print("Double", frequent_double_letters(text , alphabet))
print("Single",frequent_letters(text , alphabet))

for i in list(ciphertext):
    print(i)

