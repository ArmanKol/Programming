def standaardprijs(afstandKM):
    if afstandKM <= 0:
        totaalstandaardprijs = 0
    elif afstandKM <= 50:
        totaalstandaardprijs = 0.80*afstandKM
    elif afstandKM > 50:
        totaalstandaardprijs = 15 + 0.60*afstandKM
    return totaalstandaardprijs


def weekendrit():
    global dag
    dag = dag.lower()

    if dag == "ja":
        dag = True
    elif dag == "nee":
        dag = False


def ritprijs(leeftijd, weekendrit, afstandKM):
    if leeftijd < 12 or leeftijd >=65 and weekendrit == False:
        ritprijskorting = standaardprijs(afstandKM)*0.70
    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        ritprijskorting = standaardprijs(afstandKM)*0.65
    elif leeftijd >= 12 or leeftijd <= 65 and weekendrit == False:
        ritprijskorting = standaardprijs(afstandKM)*1
    elif leeftijd >= 12 or leeftijd <= 65 and weekendrit == True:
        ritprijskorting = standaardprijs(afstandKM)*0.60
    return ritprijskorting


leefTijd = int(input("Voer hier je leeftijd in: "))
afstandkm = int(input("Voer hier je afstand in KM in: "))
dag = input("Heb je in het weekend gereisd. Ja/Nee: ")
weekendrit()

print("De kosten zijn: €",ritprijs(leefTijd, dag, afstandkm))

