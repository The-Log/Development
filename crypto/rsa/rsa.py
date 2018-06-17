import random
from math import gcd
from random import randint
from time import time

def miller_rabin(n, k):
    ''' miller_rabin(n, k): given number n, it tests if the number is composite or prime, k times True if Prime, False if Composite'''
    d = n - 1
    s = 0
    while(d % 2 == 0): # 1st Step: find n - 1 = 2^s * m
        s = s + 1
        d = d // 2
    for i in range(k): # for accuracy 
        if(miller_rabin_trial(n, s, d) == False): # 2nd and 3rd Steps
            return False
    return True

def miller_rabin_trial(n, s, d):
    a = randint(2, n-1) # 2nd Step: find an a such that 1 < a < n -1
    b = pow(a, d, n) # 3rd Step: find b_0 = 2^s mod(n)
    if(b == 1):
        return True
    r = 0
    while(r <= s-1): # find a b_i such that (b_{i-1})^2 = (2^s)^2 mod (n)
        if(b == n-1): # if b reaches n-1, it is prime
            return True
        r = r + 1
        b = pow(b, 2, n)
    return False

def isPrime(n, k = 10):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(k):
        if miller_rabin(n, k) == False:
            return False
    return True

def find_prime(power):
    return find_prime_b(power-1, power)

def find_prime_b(lower, upper):
    x = randint(2**(lower), 2**(upper))
    if x % 2 == 0:
        x = x + 1
    while isPrime(x) == False:
        x = x + 2        
    return x

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def inv_mod(b, n):
	""" Return the modular inverse of b mod n
	 or None if gcd(b,n) > 1 """
	g, x, _ = xgcd(b, n)
	if g == 1:
            return x % n

def encrypt(plaintext, e, m):
    cipher = pow(plaintext, e, m)
    return cipher

def decrypt(ciphertext, d, m):
    plain = pow(ciphertext, d, m)
    return plain

def prepare_string(s, alphabet):
    """Usage: prepare_string(s, alphabet). Removes characters from s not in alphabet, returns new string"""
    prepared = ""
    for i in list(s):
        if (i in alphabet):
            prepared = prepared + i
    return prepared


def string_to_int(s, alphabet):
    t = 0
    for i in range(len(s)):
        t = t + pow(len(alphabet), len(s) - i - 1) * c2i(s[i], alphabet)
    return t 

def int_to_string(num, mod, alphabet):
    s = ''
    length = get_length(mod, alphabet)
    for i in range(length):
        s = i2c(num % len(alphabet), alphabet) + s
        # print(s)
        num = num // len(alphabet)
    return s

def get_length(m, alpha):
    power = 0
    while(True):
        if(len(alpha)**power > m):
            power = power - 1
            break
        else:
            power = power+1
    # print("power: %d" % power)
    return power

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

def break_message(pin, power):
    subs = []
    s = ''
    for i in range(len(pin)):
        if len(s) < power:
            s = s + pin[i]
        else:
           subs.append(s)
           s = "" + pin[i]
        #print(s)
    if len(s) > 0:
        num_of_junk = power - len(s)
        s = s + num_of_junk * ('Z') ##### change to Z #####
        subs.append(s)
    return subs

def main():
    lower = 511 #input('Your choice of low bound is two to the following power: ')
    upper = 512 #input('Your choice of upper bound is two to the following power: ')

    start = time()
    p = 605626429300532055681678497537 #find_prime(upper)
    q = 424941193007525678030099023937 #find_prime(upper)
    end = time()
    #print(p, '\n', q, '\n time', end-start) 
    print('Your two primes are:', p, '\t', q)
    mod = p * q
    totient = (p-1) * (q-1)
    print('The mod is: ', mod, ' and the totient is:', totient)
    e = 65537 #random.randrange(1, totient)

    g = gcd(e, totient)
    while g != 1:
        e = random.randrange(1, totient)
        g = gcd(e, totient)

    #d = inv_mod(e, totient)

    #print('e is:', e,' and d is:', d,'  and if this worked, this is 1:', g)


    # mod = 86518090693274675997659602491100577531533754010700509154528344441940601224095324422125553057242351043318194679920491892277959530603450993201302033735875557376123181661192976369045464156485406279786972992209311952026576666887883809461884399575753907317074031213357918245764515060159825399540741539851315401023

    
    inp = 'This is a sentence with completely normal formatting and as you can see as long as you include every character in your alphabet, it will decode perfectly with no issues whatsoever, isn\'t that exciting!'
    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;-, !\''

    '''
    print('Your input is:', inp)
    print('Your alphabet is:', alpha)

    pin = prepare_string(inp, alpha)

    print('Prepared input is:', pin)

    power = get_length(mod, alpha)

    print('Alphabet length is', len(alpha), 'and the highest power is', power)

    subs = break_message(pin, power)
    print('Broken into substrings:', subs) #['ALLWORKANDNOPLAYMA', 'KESJACKADULLBOYZZZ']

    nums = []
    for i in subs:
        nums.append(string_to_int(i, alpha))
    print('Become numbers:', nums) #[499601639309585058582440, 11543479610964610505070887]
    
    ciphered = []
    for i in nums:
        ciphered.append(encrypt(i, e, mod))
    print('Encoded to:', ciphered) # [150083385613546728423935828, 103604182818684587686420333]
    '''

    alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz., !0123456789'
    ciphered = [156175952521284255722157324843446061662387093917686026751108, 161213655142621199869921126599399686027924808360328865727342, 15691233018276555681674524287511023807685146327718243090907, 149724071042390942172850338956858434857309040011013679437481, 76480969744121351171040026278225596504381219907430176026890]

    d = inv_mod(e, totient)
    
    decoded = []
    for i in ciphered:
        decoded.append(decrypt(i, d, mod))
    print('Decoded to:', decoded) # [499601639309585058582440, 11543479610964610505070887]
    
    temp_m = []
    for i in decoded:
        temp_m.append(int_to_string(i, mod, alpha))
    print('Back to text:', ''.join(temp_m)) ### ALLWORKANDNOPLAYMAKESJACKADULLBOYZZZ


    e = 65537
    mod = 147690143426417720543026043890448472042375285573365468767128662033037446713246419100204917883446300400801225405192554010954725249626347314234029446068634707387105420955618605845881594400970904496218962357799602434736918859856803813645781043520129383769019885018939343481635017846708963422603112278784470086259
    
    inp = input()
    print('Your input is:', inp)
    print('Your alphabet is:', alpha)

    pin = prepare_string(inp, alpha)

    print('Prepared input is:', pin)

    power = get_length(mod, alpha)

    print('Alphabet length is', len(alpha), 'and the highest power is', power)

    subs = break_message(pin, power)
    print('Broken into substrings:', subs) #['ALLWORKANDNOPLAYMA', 'KESJACKADULLBOYZZZ']

    nums = []
    for i in subs:
        nums.append(string_to_int(i, alpha))
    print('Become numbers:', nums) #[499601639309585058582440, 11543479610964610505070887]
    
    ciphered = []
    for i in nums:
        ciphered.append(encrypt(i, e, mod))
    print('Encoded to:', ciphered) # [150083385613546728423935828, 103604182818684587686420333]
    

if __name__ == '__main__':
    main()

