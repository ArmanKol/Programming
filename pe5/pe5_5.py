def gemiddelde(zin):
    for word in zin:
        wordcount = len(zin.split())
        lengtezin = len(zin)
        antwoord = lengtezin / wordcount
    return antwoord

invoerzin = input("Voer hier een willekeurige zin in: ")
print("De gemiddelde lengte van de woorden in de zin is: ",gemiddelde(invoerzin))
