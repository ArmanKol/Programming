import sys
import os

def namen():
    tellen = {}
    while True:
        invoer = input("Volgende naam: ")
        invoerSplit = invoer.split()
        for naam in invoerSplit:
            if naam in tellen.keys():
                tellen[naam] += 1
            else:
                tellen[naam] = 1
        if invoer == "":
            break
    for naam in tellen:
        if tellen[naam] == 1:
            print("Er is {} student met de naam {}".format(tellen[naam], naam))
        else:
            print("Er zijn {} studenten met de naam {}".format(tellen[naam], naam))
namen()
