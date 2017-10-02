#Voer je beginstation in. Vervolgens gaat je ingevoerde waarde door een while loop en die kijkt of je ingevoerde waarde in de lijst stations voorkomt.
#Als dat het geval is dan geeft die de ingevoerde waarde terug. Zit de ingevoerde waarde niet in de lijst stations dan geeft die een foutmelding en
#Moet je opnieuw je beginstation invullen
def inlezen_beginstation(stations):
    invoerBeginstation = input("Voer je beginstation in: ")
    while invoerBeginstation != stations:
        for verschillendeStations in stations:
            if invoerBeginstation == verschillendeStations:
                return invoerBeginstation
        print("Je hebt een verkeerde beginstation ingevoerd. Probeer het opnieuw")
        invoerBeginstation = input("Voer je beginstation in: ")

#Voer je eindstation in. Er wordt gecheckt of het eindstation in de lijst stations zit en de ingevoerde eindstation hoger ligt in de lijst dan het beginstation.
#Als dat het geval is dan geeft die de ingevoerde eindstation terug.
#Zit het eindstation niet in de lijst of is de trein al de eindstation gepasseerd dan print die een foutmelding uit en zegt dat je het eindstation opnieuw moet invullen.
def inlezen_eindstation(stations, beginstation):
    invoerEindstation = input("Voer je eindstation in: ")
    while invoerEindstation != stations:
        for verschillendeStations in stations:
            if invoerEindstation == verschillendeStations and stations.index(invoerEindstation) > stations.index(beginstation):
                return invoerEindstation
        print("Deze trein komt niet in", invoerEindstation, "Probeer het opnieuw.")
        invoerEindstation = input("Voer je eindstation in: ")

#Print alle gegevens uit zoals. Hoeveel je moet betalen voor je reis. Beginstation, eindstation en
#met een while loop worden alle stations tussen beginstation en eindstation geprint.
#Ook wordt de stationsnummer geprint.
def omroepen_reis(stations, beginstation, eindstation):
    print("")
    print("Het beginstation",beginstation,"is het",str((stations.index(beginstation)+1))+"e station in het traject")
    print("Het eindstation",eindstation,"is het",str((stations.index(eindstation)+1))+"e station in het traject")

    afstandstations = (stations.index(eindstation)+1)-(stations.index(beginstation)+1)

    print("De afstand bedraagt",afstandstations,"station(s)")
    print("De prijs van het kaartje is",afstandstations*5,"euro.")
    print("")
    print("Jij stapt in de trein in:",beginstation)

    stationsBegin =  stations.index(beginstation)

    while stationsBegin != stations.index(eindstation):
        for verschillendestations in stations:
            stationsBegin += 1
            if stationsBegin < stations.index(eindstation):
                print("-",stations[stationsBegin])
            elif stationsBegin == stations.index(eindstation):
                break
    print("Jij stapt uit in:",eindstation)

stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel",
            "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)