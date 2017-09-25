import sys
import os
#Deze functie leest de regels van kluizen.txt. Daarna wordt het aantal regels bepaald met kluizenlines.
#12 - aantal regels in kluizen.txt is het aantal kluizen dat nog vrij is. Geeft aantalkluizen terug.
def toon_aantal_kluizen_vrij(invoer):
    kluizenLezen = infile.readlines()
    kluizenregels = len(kluizenLezen)
    aantalkluizen = 12 - kluizenregels
    return aantalkluizen

#Kluizen.txt wordt gelezen en de inhoud wordt omgezet in een lijst met alleen de kluisnummers.
#Alle nummers dat in res staat en nummersKluis wordt bij lijst nummersKluis eraf gehaald. Zo hou je alleen kluisnummers over die niet bezet zijn.
#Vervolgens moet je een kluiscode intypen en dat wordt dan samen met de kluisnummer opgeslagen in kluizen.txt.
def nieuwe_kluis(invoer):
    kluizenLezen = infile.readlines()
    nummersKluis = [1,2,3,4,5,6,7,8,9,10,11,12]
    res = []
    for kluisnummers in kluizenLezen:
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

#Kluis wordt geopend door middel van kluisnummer en kluiscode. De combinatie gaat door een loop en als de combinatie klopt krijg je een bericht.
def kluis_openen(invoer):
    kluizenLezen = infile.read()
    kluisnummer = str(input("Toets kluisnummer in: "))
    kluiscode = str(input("Wat is je kluiscode: "))
    kluiscombinatie = kluisnummer+";"+kluiscode
    for kluizen in kluizenLezen:
        if kluiscombinatie in kluizenLezen:
            return print("Je hebt toegang tot je kluis")
        else:
            return print("Je hebt geen toegang.")

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
elif invoer == 0 or invoer >= 4:
    print("Je hebt geen geldige nummer gekozen.")

infile.close()