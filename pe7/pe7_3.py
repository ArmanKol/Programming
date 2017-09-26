import os
import sys

cursus = {"Piet":9.0, "Henk": 4.2, "Martijn":9.5, "Jonas":9.2, "Diederik":8.8, "Olaf":7, "Max":9.2, "Jolyon":1.1,"Daniel":9.1,"Mustafa":10}

def hogecijfers(cursus):
    for cijfers in cursus.values():
        if cijfers > 9 in cursus.values():
            print(cursus.items(cijfers))
hogecijfers(cursus)
