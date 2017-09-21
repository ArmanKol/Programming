import sys
import os
def seizoen(maand):
    winter = [1, 2, 12]
    lente = [3, 4, 5]
    zomer = [6, 7, 8]
    herfst = [9, 10, 11]
    if maand in winter:
        return "Winter"
    elif maand in lente:
        return "lente"
    elif maand in zomer:
        return "zomer"
    elif maand in herfst:
        return "herfst"

maandnummer = int(input("Geef een maandnummer: "))
print(seizoen(maandnummer))