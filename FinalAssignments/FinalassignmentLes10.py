import xmltodict

#Een filename wordt opgegeven. Deze functie read de file en vervolgens krijg je die returned.
def XMLlezen(filename):
    with open(filename, "r") as myXMLfile:
        reader = myXMLfile.read()
        xmldirectory = xmltodict.parse(reader)
        return xmldirectory

#Deze functie pakt met een loop alle codes en types. Dat wordt uitgeprint en opgeslagen in een variable. Die variable met alle codes en types worden gereturned.
def LezenCodeTypes():
    for CodeTypes in stations:
        PrintCodeTypes = print(CodeTypes["Code"], "-",CodeTypes["Type"])
    return PrintCodeTypes

#Deze functie pakt met een loop alle namen en codes. Dat wordt uitgeprint en opgeslagen in een variabel. Die variabel met alle codes en namen worden gereturned.
def LezenNamenCode():
    for verschillendeLangeNamen in stations:
        PrintNamen = print(verschillendeLangeNamen["Code"],"-",verschillendeLangeNamen["Namen"]["Lang"])
    return PrintNamen

#Deze functie doorloopt het bestand stations.xml. Als het type Synoniem["Synoniemen"] niet gelijk is aan het type <class "NoneType"> dan wordt de
#stationscode en het synoniem uitgeprint. Vervolgens wordt de stationscode en synoniem gereturned.
def LezenSynoniem():
    SynoniemNoneType = "<class 'NoneType'>"
    for Synoniem in stations:
        if str(type(Synoniem["Synoniemen"])) != SynoniemNoneType:
            PrintSynoniem = print(Synoniem["Code"], "-", Synoniem["Synoniemen"])
    return PrintSynoniem

stationsStore = XMLlezen("stations.xml")
stations = stationsStore["Stations"]["Station"]

print("Dit zijn de codes en types van de",len(stations),"stations")
LezenCodeTypes()

print()
print("Dit zijn alle stations met één of meer synoniem:")
LezenSynoniem()

print()
print("Dit is de lange naam van elk station:")
LezenNamenCode()
