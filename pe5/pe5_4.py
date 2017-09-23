import os
import sys
import datetime

outfile = open("Hardlopers.txt", "a")
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %y, %H:%M:%S, ")
invoer = input("Naam van de hardloper: ")
outfile.write(s +invoer)
outfile.write("\n")
outfile.close()

