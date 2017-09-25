import sys
import os
#Deze functie leest kluizen.txt en splitst de inhoud. Daarna wordt het aantal kluizen bepaald en returned.
def toon_aantal_kluizen_vrij(invoer):
    kluizenread = infile.read()
    aantalkluizen = kluizenread.count(";")
    kluizen = 12 - aantalkluizen
    infile.close()
    return kluizen

#Kluizen.txt wordt gelezen en de inhoud wordt omgezet in een lijst met alleen de kluisnummers.
#Vervolgens moet je een kluiscode intypen en dat wordt dan samen met de kluisnummer opgeslagen.
def nieuwe_kluis(invoer):
    kluizenread = infile.readlines()
    nummersKluis = [1,2,3,4,5,6,7,8,9,10,11,12]
    res = []
    for kluisnummers in kluizenread:
        Nieuw = kluisnummers[:2]
        GetalNieuw = Nieuw.strip(";")
        res.append(int(GetalNieuw))
        nummersKluis = [x for x in nummersKluis if x not in res]
    if len(nummersKluis) > 0:
        kluiscode = input("Type hier je kluiscode voor je nieuwe kluis in: ")
        laagsteNummer = min(nummersKluis)
        kluiscombinatie = ("{};{}".format(laagsteNummer, kluiscode))
        print("Het is gelukt. Je hebt kluisnummer:", laagsteNummer)
        outfile = open("kluizen.txt", "a")
        outfile.write(kluiscombinatie)
        outfile.write("\n")
        outfile.close()
    else:
        print("Er zijn geen kluizen meer over.")
    infile.close()

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
    infile.close()

infile = open("kluizen.txt", "r")

print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
print("2: Ik wil een nieuwe kluis")
print("3: Ik wil even iets uit mijn kluis halen")

invoer = int(input("Kies een nummer: "))

if invoer == 1:
    print("Er zijn nog:",toon_aantal_kluizen_vrij(invoer),"kluizen vrij")

if invoer == 2:
    nieuwe_kluis(invoer)

if invoer == 3:
    kluis_openen(invoer)
else:
    print("Je hebt geen geldige nummer gekozen.")