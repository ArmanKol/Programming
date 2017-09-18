import os
import sys
#Nog niet af.
def convert(celsius):
    fahrenheit = celsius * 1.8 +32
    return fahrenheit

def table():
    for temperatuur in range (-30, 50,10):
        print("{:5} {:10}".format(temperatuur*1.8 +32, temperatuur))

print(table())


