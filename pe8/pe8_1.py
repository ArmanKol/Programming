import os
import sys

bruin = {"Boxtel", "Best", "Beukenlaan","Helmond't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}

print(bruin.intersection(groen))
print(bruin.difference(groen))
print(bruin.union(groen))
