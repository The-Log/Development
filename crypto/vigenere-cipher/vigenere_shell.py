#from subcipher import *
from math import gcd
from collections import Counter

def c2i(c, alphabet):
    """Returns the index of c in the string alphabet, starting at 0"""
    return alphabet.index(c)

def i2c(i, alphabet):
    """Returns the character at index i in alphabet"""
    return alphabet[i] % len(alphabet)

def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    prepared = ""
    for i in list(s.upper()):
        if (i in alphabet):
            prepared = prepared + i
    return prepared


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

def index_of_coincidence(ciphertext, alphabet):
    """Returns index of coincidence of a certain block of ciphertext"""
    n = len(ciphertext)
    freq = Counter(ciphertext)
    ioc = 0
    for i in list(alphabet):
        ioc = ioc + freq[i] * (freq[i] - 1)
    ioc = 1/n * 1/(n-1) * ioc
    return ioc
        
def friedman_test(ciphertext, alphabet):
    """Calls index_of_coincidence, then returns the predicted value for keyword length from the friedman test
    using that value"""
    n = len(ciphertext)
    ioc = index_of_coincidence(ciphertext, alphabet)
    l = (.027 * n)/ ((n-1)* ioc + .0655-.0385*n)
    return l
    
def kasiski_test(ciphertext, alphabet):
    trigraphs = []
    distances = []
    for index in range(len(ciphertext) - 3):
        tg = ciphertext[index:index + 3]
        if tg not in trigraphs:
            trigraphs.append(tg)
        else:
            first = ciphertext.index(tg)
            distances.append(index-first)
    print(distances)
        
            
    #Code partially provided
    """Finds gcd of most common distances between repeated trigraphs
    Recommended strategy: loop through the ciphertext, keeping a list of trigraphs and a list of distances in this way:
    1) When encountering a new trigraph add it to the trigraph list
    2) When encountering a repeat add the distance from current index to first index of that trigraph to the list of distances"""
    # Here, write code to create the array of distances:

    # Code is provided to find the gcd of any common distances appearing at least twice, just add your array:
    
    dCount = Counter(distances)
    topCount = dCount.most_common(6)
    my_gcd = topCount[0][0]
    for index in range(1, len(topCount)):
        if topCount[index][1] > 1:
            my_gcd = gcd(my_gcd, topCount[index][0])
    return my_gcd
    
    
def run_key_tests(ciphertext, alphabet): #Code provided
    """Runs Friedman and Kasiski tests and formats the output nicely"""
    friedman = friedman_test(ciphertext, alphabet)
    kasiski = kasiski_test(ciphertext, alphabet)
    out = "Friedman test gives: " + str(friedman) + " and Kasiski gives this as the most likely: " + str(kasiski);
    return out

def make_cosets(text, n):
    """Makes cosets out of a ciphertext given a key length; should return an array of strings"""
    cosets = [""] * n
    for i in range(len(text)):
        cosets[i%n] = cosets[i%n] + text[i]
    return cosets

def rotate_list(old_list):  #Code provided
    """Takes the given list, removes the first element, and appends it to the end of the list, then returns the new list"""
    new_list = old_list[:]
    new_list.append(old_list[0])
    del new_list[0]
    return new_list

def find_total_difference(list1, list2):
    """Takes two lists of equal length containing numbers, finds the difference between each pair of matching
    numbers, sums those differences, and returns that sum"""
    t = 0
    for i in range(len(list1)):
        t = t + abs(list2[i] - list1[i])
    return t

def find_likely_letters(coset, alpha, eng_freq):
    """Finds the most likely shifts for each coset and prints them
    Recommended strategy: make a list of the frequencies of each letter in the coset, in order, A to Z.
    Then, alternate using the find total difference method (on your frequencies list and the standard english
    frequencies list) and the rotate list method to fill out a new list of differences.  This makes a list of
    the total difference for each possible encryption letter, A to Z, in order.
    Then, find the indices of the smallest values in the new list, and i2c them for the most likely letters."""
    
    tempfreq = Counter(coset)
    freq = []
    for i in alpha:
        freq.append(tempfreq[i]/len(coset))        
    tot_dist = []
    for i in range(26):
        tot_dist.append(find_total_difference(freq, eng_freq))
        freq = rotate_list(freq)
    a = [x for _,x in sorted(zip(tot_dist,alpha))]
    letter1 = a[0]
    letter2 = a[1]
    return "the most likely letter is: " + letter1 + " followed by: " + letter2

def crack(ciphertext, alpha, eng_freq):  #Code provided
    """User-friendly walkthrough of decoding methods"""
    print("Your cipher text is: " + ciphertext)
    out = run_key_tests(ciphertext, alpha)
    print(out)
    x = int(input("Choose the key length you'd like to try: "))
    cosets = make_cosets(ciphertext, x)
    for index in range(len(cosets)):
        print("For coset " + str(index + 1) + ", " + find_likely_letters(cosets[index], alpha, eng_freq) + ".")
    s = input("Type the key you would like to use to decipher: ")
    print(vigenere_decode(ciphertext, s, alpha))
    print()




alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751,
            .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]

example = "UZRZEGNJENVLISEXRHLYPYEGTESBJHJCSBPTGDYFXXBHEEIFTCCHVRKPNHWXPCTUQTGDJHTBIPRFEMJCNHVTCFSAIIJENREGSALHXHWZWRZXGTTVWGDHTEYXISAGQTCJPRSIAPTUMGZALHXHHSOHPWCZLBRZTCBRGHCDIQIKTOAAEFTOPYEGTENRAIALNRXLPCEPYKGPNGPRQPIAKWXDCBZXGPDNRWXEIFZXGJLVOXAJTUEMBLNLQHGPWVPEQPIAXATYENVYJEUEI"

#print(make_cosets(example, 6))

# For the example, the key is "PLANET" and the plaintext is:
# "For many years the known planets of our solar system were mercury, venus, earth, mars, jupiter, saturn, uranus, neputne, and pluto.  However, it is now true that many people think pluto should no longer be considered a named planet.  New planets are currently being discovered, and it is very likely that many more will be in the near future."

#Try this:
crack(example, alpha, eng_freq)

#Once everything works, uncomment the following six lines and crack some ciphertexts!
c1 = "RVCQWMYFULRIKPFMQEMTJJOCLHYVHNFONGOGUFCRWHEPYAOOQSQCBYCRGMFYRSMRQUQSMYBXGKULHCRHIZSMSTZGQCCBNJMFMBARVURHBGGQFCFCHBGBAUCLIGQGHBMINPSFWWHECHPOHBCGAVULQYRCJPCXSQYECIBRCQHLGPORWILGQGHBQAUJZVGHMMTNCLNGHNPIFWBYCRMRCVCEOGHYJCHEWHMHBCFYYFFGSLRSMRGGWDFYWHRSRRKUQHIMGBMFNYBXGHGYRYZCNFTLGSXKOHYBXIOMGGEGTLCOEMINYBXEWPCHYPFCZZYYBMUSLQ"
c2 = "EFMREXHTGRQQVDODIPQSIVVNURSUVVNGNXRRIOIBEPOZNISWDRIOEOWVVYAVVIDFJFTYQDPFRKQMQCCFQBQXNRTKYRRHRCQWTXVZNIZVRDCEODSHZVCWDEENVCQWTXVVRRBSJTRMUZVRIIAOWMQIZNXYPYGJAEDMYKKIGCWXEYAUKRDNPSKCHHXVLQZMQILNFOVVVRNFSRJIVNGBEWKEGCVKRTZTJWWYGIIHSGDVZOPYJUGHUKBIPGETUYJDNXOTSXKOJIPMPXFZNIDLHKICQBVHEKNGCWDPURGCSXTTEUMSQULMRDMRPRNFSQSNVMGXXDVZOPMSPOFNNIVHHVRTOHWQRSEYHLPXOHKPJQIIVRQVKEAVKVJGKPTYKUCDMKXKOCEGWKKHUFUTMIFQUEKCAUKKTGXMQQEEQBQRTVPTYKUCDMKXKOCEGWKKHUKHGZYURFSGYJSTFGTKQPKEGKCXRHZNFKWHSLEPMIRHZNUDVXEKIQXWWJRTYSPOCLTQWEWGGETPSUOZNIKWSGTIHSGWCJKQBWRNMIPQEJKMEPZVRDCEODLHRIOEOWVQWPTYKUCDMKXKWJLSQPXHPIESEMUGJEZZIUVZSGSRPCEYFSJIGIEPDWXDAEEDWLPTLWNMQIBNQGPHFXEQPXKGRPRVMFCKIQXHRORIPCTHEZANSDHFRLIYVLVYMUKRGHFROKPOQXIEBIOCKEFDEVMJIPMPXFVTGCXLPXDGLYJIZNIKRGORIPDELPZNIDLHUFUTMIFQUEKWTOGDEPDEWKFNQPXKGSUKVHVAJTGWEQFDAPKKHOVNVYJGGIIXOHDTKIHKGWUJUEREVORCJSRHEFDGYJFQDPWDIURIOIBEPUKHGCIPKXHVLIFQESKNIUGUPCBXRHKHGZVRIIAOWMQIGRQMIVUSUVYJWGETJOXHTDSQPXZCIEFOZHNFPOORWKJUUOHIQITJSWOCIGGBTUQTEUCALVYTJOXHTDPTYKUCDMKXKLOGLGWIQVRTKYRRTTOFSRJTVSGBZHFWOTDLHCTTWKPZTZTKXKRHJOWBGHEFDGCSIVNATOIQIZNGOVLPXCQWFLPVSGXKLPVETSRJVVCJXMTWVSYSXKUFFVGEUGUEXOPRRDEPDTUCTTKMIV"
c3 = "OPKLNPCAVGYQRPKSAJUMYIUGVJHETIRRYWRHEEXQVBYEGSEIZVJSSMKEXWRSHVVHKWYXRVKSJTGVTIWSMQTHBSIHDAVPNCYEYJKIAXRGFMJXBXYIRIRPVXUIKQIXRHJMHXRCNRVRJZSSHWWEXMSSEIKLVVGQRXIIRQJIGLVJVKKSSEDEIWLEOSLXAWXXLJZZZEOXUEYIVDEFYETOHWAWGETLZITHEYXKZLRCUEEHNWSISIRXPZKWJMEWOWTQNHVJJZZLRWKEDZYMGARWIWAWRXICDVMXUICMABKZRRRXOPKFRWKSABOQRWZXRIYWRPUSHEUVXMEKVVJEGTIINMTXGLVIGMIXEMTGPZXIAXNENKAXBJWHPZORTHRCGQMLGLFYMAOXJEJTVZZSSXYIZKURBQPHMQBIVRGVZXGVNXZSINUVUEKIRMKOGLVJGIZANWJIQMTJYMXLOAATNRUADVYXBRNLJEGWGLZVOGTMAIRRYPGHNZRVDKUWRYCGZZGFBZVLDAXMTLKEISRIJIEXNTUAYCIINBORTWVZZZGPGMDINWTXUINETWTINGYPVVJMAKFTKWYMGIKLZTOJGWYEABZLRTFWOMXAVXYXCMKRBVDSPALEPIXEUMJJESDXCMCEYPZXRIYSAIFJOPUWRTZGOCXIFAYMXPGVRWFGJVZVVZVHOPGXGLVITMYJBPCSRGUYNFFYOENIACFYHWBIOMXFMWZLRVZWRIZGUMEKTWAXUITEKBOSAFVRZIZLVXIEI"
#crack(c1, alpha, eng_freq)
#crack(c2, alpha, eng_freq)
#crack(c3, alpha, eng_freq)
