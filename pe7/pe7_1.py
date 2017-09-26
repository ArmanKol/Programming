import sys
import os

def sum():
    total = 0
    res = []
    while True:
        invoerGetal = input("Geef een getal: ")
        if invoerGetal == "0":
            break
        else:
            total += int(invoerGetal)
            res.append(int(invoerGetal))
    print("Er zijn",len(res),"getallen ingevoerd, de som is:",total)
sum()

