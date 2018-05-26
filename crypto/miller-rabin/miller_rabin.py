from random import *
from primefac import *
from timeit import default_timer as timer

def miller_rabin(n, k): 
  d = n-1
  s = 0
  while(d % 2 == 0):
    s = s + 1
    d = d // 2
  for x in range(k):
    if(miller_rabin_trial(n,s,d) == False):
      return False
  return True

def miller_rabin_trial(n,s,d):
  a = randint(2, n-1)
  x = pow(a,d,n)
  if(x == 1):
    return True
  r = 0
  while(r<=s-1):
    if(x == n-1):
      return True
    r = r+1
    x = pow(x,2,n)
  return False

def check_square(n): #2
  x = int(n**0.5)
  while(x**2 < n):
    x = x+ 1
  if(x**2 == n):
    return True
  return False
  
def odd_primes(n): #3
  x = int(n**(.5))+1
  while(True):
    if(check_square(x**2 - n)):
      y = (x**2 - n)**(.5)
      return (int(x-y), int(x+y))
    else:
      x=x+1
  return null
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
          
def run_trial(e): #4
  start1 = timer()
  p = nextprime(e)
  q = nextprime(e)
  stop1 = timer()
  dif1 = stop1 - start1 
  print(dif1)
  n = p*q 
  start2 = timer()
  factors = odd_primes(n)
  stop2 = timer()
  dif2 = stop2 - start2 
  print(dif2)
  
def run_multiple_trials(e):
  avg = 0
  for i in range(10):
    start = timer()
    p = find_prime(e) #nextprime(e)
    q = find_prime(e) #nextprime(e)
    n = p*q 
    stop = timer()
    avg += stop - start
  avg = avg/10
  print("Finding primes took %f" % avg)
  avg = 0
  for i in range(10):
    start = timer()
    odd_primes(n)
    stop = timer()
    avg += stop - start
  avg = avg/10
  print("Factoring product took %f" % avg)
  
def run_trials_2(power):
  start1 = timer()
  y = randint(2**(power-1), 2**power)
  x = nextprime(y)
  stop1 = timer()
  dif1 = stop1 - start1 
  print(dif1)
  start1 = timer()
  x = factorint(y)
  stop1 = timer()
  dif1 = stop1 - start1 
  print(dif1)


run_trial(1700)
#run_multiple_trials(30)