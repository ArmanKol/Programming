age = int(input("Geef je leeftijd: "))
paspoort = input("Nederlands paspoort: ")

if age >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
elif age < 18 and paspoort == "ja":
    print("Je mag niet stemmen.")
elif age >= 18 and paspoort == "nee":
    print("Je mag niet stemmen.")
elif age < 18 and paspoort == "nee":
    print("Je mag niet stemmen.")
