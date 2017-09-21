import sys
import os

def vierletter(lijst):
    res = []
    for woorden in lijst:
        if len(woorden) == 4:
            res.append(woorden)
    print(res)

invoer = eval(input("Geef lijst met minimaal 10 strings: "))
lijst1 = ["boter", "kaas", "bier", "pizza","thee", "drop", "koek", "cola", "boterham", "stamppot"]


vierletter(invoer)