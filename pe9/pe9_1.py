hotelkosten = 4356
try:
    aantalpersonen = int(input("Met hoeveel personen reis je: "))
    kostenperpersoon = hotelkosten / aantalpersonen
    if aantalpersonen <= 0:
        print("Negatieve getallen zijn niet toegestaan!")
    elif aantalpersonen > 0:
        print("Je betaalt","\u20AC",kostenperpersoon,"per persoon")
except ZeroDivisionError:
    print("Delen door nul kan niet.")
except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except:
    print("Onjuiste invoer")