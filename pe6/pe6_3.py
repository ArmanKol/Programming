import sys
import os

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = []
invoer = invoer.split("-")
for cijfers in invoer:
    if cijfers in invoer:
        lijst.append(int(cijfers))
print("Gesorteerde list van ints:", sorted(lijst))
print("Grootste getal:", max(lijst), "en Kleinste getal:", min(lijst))
print("Aantal getallen:", len(lijst), "en Som van de getallen:", sum(lijst))
print("Gemiddelde:", sum(lijst) / len(lijst) )



