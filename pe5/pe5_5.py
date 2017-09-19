def gemiddelde(zin):
    for word in zin:
        wordcount = len(zin.split()) #splitst de woorden en neemt daarna het aantal woorden in de lijst
        lengtezin = len(zin) # Berekent alle letters in de lijst
        antwoord = lengtezin / wordcount
    return antwoord

invoerzin = input("Voer hier een willekeurige zin in: ")
print("De gemiddelde lengte van de woorden in de zin is: ",gemiddelde(invoerzin))
