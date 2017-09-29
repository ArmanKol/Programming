def code(invoerstring):
    nieuweBeveiligingsCode = ""
    for char in invoerstring:
        nieuwecode = ord(char) + 3
        omzetting = chr(nieuwecode)
        print(omzetting, end="")


gebruiker = input("Wat is je voornaam: ")
beginstation = input("Beginstation: ")
eindstation = input("Eindstation: ")
GebBeginEind = gebruiker+beginstation+eindstation
code(GebBeginEind)