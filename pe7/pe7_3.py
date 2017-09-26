import os
import sys

cursus = {"Piet":9.0, "Henk": 4.2, "Martijn":9.5, "Jonas":9.2, "Diederik":8.8, "Olaf":7, "Max":9.2, "Jolyon":1.1,"Daniel":9.1,"Mustafa":10}
itemsCursus = cursus.items()
valueCursus = cursus.values()

def hogecijfers(cursus):
    for naam,cijfer in itemsCursus:
        if cijfer > 9.0 in valueCursus:
            print(naam, cijfer)
hogecijfers(cursus)
