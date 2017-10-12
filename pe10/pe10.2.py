import time

def verdubbelB():
    global b
    b = b + b

def f(y):
    return 2*y +1

def g(x):
    return 5 + x + 10

b = 7
verdubbelB()
print(b)
print(time.strftime(("%H:%M:%S")))
print(f(3)+g(3))

