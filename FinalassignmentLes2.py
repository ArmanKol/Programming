def standaardprijs(afstandKM):
    if afstandKM > 50:
        totaalstandaardprijs = 15 + 0.60*afstandKM
    elif afstandKM <= 50:
        totaalstandaardprijs = 0.80*afstandKM
    elif afstandKM <= 0:
        totaalstandaardprijs = 0
    return totaalstandaardprijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >=65 and weekendrit in ("nee"):
        ritprijskorting = standaardprijs(afstandKM)*0.70
        if leeftijd < 12 or leeftijd >= 65 and weekendrit in ("ja"):
            ritprijskorting = standaardprijs(afstandKM)*0.65
    elif leeftijd >= 12 or leeftijd <= 65 and weekendrit in ("nee"):
        ritprijskorting = standaardprijs(afstandKM)*1
        if leeftijd >= 12 or leeftijd <= 65 and weekendrit in ("ja"):
            ritprijskorting = standaardprijs(afstandKM)*0.60
    return ritprijskorting

leefTijd = int(input("Voer hier je leeftijd in: "))
afstandkm = int(input("Voer hier je afstand in KM in: "))
dag = str(input("Heb je in het weekend gereisd: "))
print(str("De kosten zijn: €"),ritprijs(leefTijd, dag, afstandkm))

