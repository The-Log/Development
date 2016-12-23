import random

def random_results():
    print("Time (secs) \t Speed (mph)")
    for i in range(41):
        if (i <= 3):
            print(str(i * 15) + "\t " + str(random.randint(10,30)))
        elif (i > 3 and i < 15):
            print(str(i * 15) + "\t " + str(random.randint(45,60)))
        else:
            print(str(i * 15) + "\t " + str(random.randint(55,65)))


random_results()
