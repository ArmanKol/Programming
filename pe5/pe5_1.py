import os
import sys

def convert(celsius):
    fahrenheit = celsius * 1.8 +32
    return fahrenheit

def table():
    print("{:12} {:5}".format("F", "C"))
    for temperatuur in range (-30, 50,10):
        print("{:5} {:10}".format(temperatuur*1.8 +32, float(temperatuur)))
table()


