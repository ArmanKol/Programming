import csv

def filereader(filename):
    with open(filename, "r") as Producten:
        reader = csv.reader(Producten, delimiter=";")

        lst2d = []
        for gegevens in reader:
            lst2d.append(gegevens)
        lst2d.pop(0)
        return lst2d

lst2D = filereader("producten.csv")

tempindex = 0
hoogsteprijs = -10000
for x in range(0,len(lst2D)):
    if float(lst2D[x][4]) > hoogsteprijs:
        hoogsteprijs = float(lst2D[x][4])
        tempindex = x
print("Het duurste artikel is",lst2D[tempindex][2],"en die kost",hoogsteprijs,"euro")

tempindex = 0
kleinstevoorraad = 999999
somvoorraad = 0
for x in range(0,len(lst2D)):
    somvoorraad = somvoorraad + int(lst2D[x][3])
    if int(lst2D[x][3]) < kleinstevoorraad:
        kleinstevoorraad = int(lst2D[x][3])
        tempindex = x

print("Er zijn slechts", lst2D[tempindex][3],"exemplaren in voorraad van het product met nummer",lst2D[tempindex][0])
print("In totaal hebben wij",somvoorraad,"producten in ons magazijn liggen.")


