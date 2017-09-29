import os
import sys

def ticket (filename):
    dctTickers = {}
    infile = open(filename, "r")
    lines =  infile.readlines()

    for line in lines:
        lineSplit = line.split(":")
        dctTickers[lineSplit[0]] = lineSplit[1].strip()
    return dctTickers

def reverseDict(dctInput):
    dctReverse = {}

    for naam in dctInput.keys():
        afkorting = dctInput[naam]
        dctReverse[afkorting] = naam
    return dctReverse

dctTickets = ticket("tickerSymbols.txt")
dctTicketsRev = reverseDict(dctTickets)
invoer = input("Geef een bedrijfsnaam of afkorting:")

if invoer in dctTickets.keys():
    print("Afkorting is:", dctTickets[invoer])
elif invoer in dctTicketsRev.keys():
    print("Naam is:", dctTicketsRev[invoer])