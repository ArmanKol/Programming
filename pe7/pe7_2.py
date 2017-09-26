import sys
import os

def vierletter():
    while True:
        woord = input("Geef een string van vier letters: ")
        if len(woord) < 4 or len(woord) > 4:
            print(woord, "Heeft", len(woord), "letters")
        elif len(woord) == 4:
            print("Inlezen van correcte string:", woord, "is geslaagd")
            break
vierletter()