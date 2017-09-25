import sys
import os
#NOG NIET AF

#Deze functie leest kluizen.txt en splitst de inhoud. Daarna wordt het aantal kluizen bepaald en returned.
def toon_aantal_kluizen_vrij(invoer):
    kluizenread = infile.read()
    aantalkluizen = kluizenread.count(";")
    kluizen = 12 - aantalkluizen
    return kluizen

def nieuwe_kluis(invoer):
    kluizenread = infile.readlines()
    nummersKluis = [1,2,3,4,5,6,7,8,9,10,11,12]
    res = []
    for kluisnummers in kluizenread:
        Nieuw = kluisnummers[:2]
        GetalNieuw = Nieuw.strip(";")
        res.append(int(GetalNieuw))
    nummersKluis = [x for x in nummersKluis if x not in res]
    if nummersKluis != 0:
        kluiscode = input("Type hier de code voor je nieuwe kluis in: ")

#Kluis wordt geopend door middel van kluisnummer en kluiscode. De combinatie gaat door een loop en als de combinatie klopt krijg je een bericht.
def kluis_openen(invoer):
    kluizenread = infile.read()
    kluisnummer = str(input("Toets kluisnummer in: "))
    kluiscode = str(input("Wat is je kluiscode: "))
    kluiscombinatie = kluisnummer+";"+kluiscode
    for kluizen in kluizenread:
        if kluiscombinatie in kluizenread:
            return print("Je bent in je kluis")
        else:
            return print("Je bent niet in je kluis")


def kluis_teruggeven(invoer):
    kluizenread = infile.read()
    kluisnummer = input("Toets kluisnummer in: ")
    kluiscode = input("Wat is je kluiscode: ")
    kluiscombinatie = kluisnummer+";"+kluiscode
    if kluiscombinatie in kluizenread:
        kluizenread.replace(kluiscombinatie, "")
        print("Je kluis is terug gegeven.")
    else:
        print("Je kluiscombinatie klopt niet.")

infile = open("kluizen.txt", "r")

print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")
print("4: Ik geef mijn kluis terug")

invoer = int(input("Kies een nummer: "))

if invoer == 1:
    print("Er zijn nog:",toon_aantal_kluizen_vrij(invoer),"kluizen vrij")

if invoer == 2:
    nieuwe_kluis(invoer)

if invoer == 3:
    kluis_openen(invoer)

if invoer == 4:
    kluis_teruggeven(invoer)