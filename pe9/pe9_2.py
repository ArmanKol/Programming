import datetime
import csv

bestand = "inloggers.csv"
vandaag = datetime.datetime.today()
formatVandaag = vandaag.strftime("%a %d %b %y at %H:%M")

with open(bestand, "w", newline="") as inlogGegevens:
    writer = csv.writer(inlogGegevens, delimiter=";")
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((formatVandaag, voorl, naam, gbdatum, email))