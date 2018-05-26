from hill_cipher import *

db = open("passwords-v4.txt","r")
alphabet = "".join(chr(x) for x in range(33,94))
print(alphabet)
mod = len(alphabet)
print(mod)

c_p = open("common-passwords.txt","r")
cpl = []
for l in c_p:
    s = l.strip().upper()
    if len(s) >= 6:
        cpl.append(s)
    
l = []
for line in db.readlines():
    line = line.strip()
    (un, pw) = line.split()
    un = prepare_string(un, alphabet)
    pw = prepare_string(pw, alphabet)
    l.append((un, pw))

all_mats = set()

for i in l:
    for cp in cpl:
        
        m_b = get_encoding(cp, i[1], alphabet, mod)
        password = (hill_decode(i[1], m_b, alphabet))
        
        if cp == password[0:len(cp)]:
            #all_mats.add(str(m_b))
            print(i[0], '\t', password, '\t', m_b)
            #break
'''
for i in l:
    for crib in cpl:
        print(get_bruteforce(crib, i[1], alphabet, mod))
'''
