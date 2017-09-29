import random

def monopolyworp():
    dobbelsteen1 = random.randrange(1, 7)
    dobbelsteen2 = random.randrange(1, 7)
    counter = 0
    print(dobbelsteen1, "+", dobbelsteen2, "=", (dobbelsteen1 + dobbelsteen2), end=" ")
    while dobbelsteen1 == dobbelsteen2:
        counter += 1
        if counter >= 3:
            print("Direct naar de gevangenis")
            break
        if dobbelsteen1 == dobbelsteen2:
            print("dubbel")
        dobbelsteen1 = random.randrange(1, 7)
        dobbelsteen2 = random.randrange(1, 7)
        print(dobbelsteen1, "+", dobbelsteen2, "=", (dobbelsteen1 + dobbelsteen2), end=" ")

monopolyworp()