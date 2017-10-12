import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        read = myXMLFile.read()
        xmldictionary = xmltodict.parse(read)
        return xmldictionary

productendict = processXML("producten.xml")
producten = productendict["artikelen"]["artikel"]

for artikel in producten:
    print(artikel["naam"])
