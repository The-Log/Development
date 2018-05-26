f = open('badword.txt', 'r')
badwords = f.read().split('\n')
i = 0

def output(s=None):
    if s == None:
        s = input("Enter a phrase: ")
        i = 1
    prev = ""
    while(not prev == s):
        print(s)
        print(s.count('e'))
        print(s[::-1])
        print(s.replace('s','*'))
        print(s.upper())
        for i in badwords:
            if i in s and len(i) > 0:
                print("Be Nice")
                break
        if len(s) > 50:
            print("TOO LONG")
        prev = s
        print("")
        if i == 1:
            s = input("Enter a phrase: ")

if __name__ == '__main__':
    temp = input("Enter a phrase: ")
    l = temp.split(" ")
    for i in l:
        output(i)
