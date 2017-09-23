import os
import sys

infile = open("kaartnummers.txt", "r")
kaartnummers = infile.read()
infile.close()
kaartnummers = kaartnummers.replace("\n", ",")
kaartnummers = kaartnummers.split(",")
print(kaartnummers[1], "heeft kaartnummer:", kaartnummers[0])
print(kaartnummers[3], "heeft kaartnummer:", kaartnummers[2])
print(kaartnummers[5], "heeft kaartnummer:", kaartnummers[4])
print(kaartnummers[7], "heeft kaartnummer:", kaartnummers[6])
print(kaartnummers[9], "heeft kaartnummer:", kaartnummers[8])
print(kaartnummers[11], "heeft kaartnummer:", kaartnummers[10])

