import os
import sys
#NOG NIET AF
infile = open("kaartnummers.txt", "r")

for hoogstecijfer in infile:
    hoogste = max(infile)
infile.close()

infile = open("kaartnummers.txt", "r")
kaartnummers = infile.read()
aantalregels = kaartnummers.count(",")
hoogstekaartnummer = hoogste[:6]

infile.close()

print("Deze file telt " + str(aantalregels) + " regels")
print("Het grootste kaartnummer is: " + hoogstekaartnummer + " en staat op regel ")