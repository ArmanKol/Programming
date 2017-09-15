#som neemt de getallen en telt ze vervolgens bij elkaar op. Daarna wordt het opgetelde getal teruggegeven.
def som(getal1, getal2, getal3):
    getallen = getal1 + getal2 + getal3
    return getallen

nummer1 = int(input("Geef getal1: "))
nummer2 = int(input("Geef getal2: "))
nummer3 = int(input("Geef getal3: "))
antwoord = som(nummer1, nummer2, nummer3)
print("Getal 1,2 en 3 worden opgegeteld en dat is: " + str(antwoord))