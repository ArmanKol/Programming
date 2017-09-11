age = int(input("Geef je leeftijd: "))
paspoort = input("Nederlands paspoort: ")

if age >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
elif age < 18:
    print("Je bent niet oud genoeg")
elif paspoort == "nee":
    print("Je hebt geen Nederlands paspoort.")
