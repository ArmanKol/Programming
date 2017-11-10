#Hier wordt het aantal KM keer de prijs gedaan. Vervolgens wordt de totaalstandaardprijs returned.
def standaardprijs(afstandKM):
    if afstandKM <= 0:
        totaalstandaardprijs = 0
    elif afstandKM <= 50:
        totaalstandaardprijs = 0.80*afstandKM
    elif afstandKM > 50:
        totaalstandaardprijs = 15 + 0.60*afstandKM
    return totaalstandaardprijs

#Hier wordt gekeken of dag die je bij input invoerd gelijk is aan "ja" of "nee". Bij ja krijg je een True en bij nee een False
def weekendrit():
    global dag
    dag = dag.lower()

    if "ja" in dag:
        return True
    elif "nee" in dag:
        return False

#Hier neemt die de leeftijd mee en bekijkt bij welke if statement het hoort. Ook wordt er gekeken naar of het een weekendrit is of niet. Vervolgens wordt de nieuwe prijs uitgerekent
#en die prijs wordt gereturned.
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

