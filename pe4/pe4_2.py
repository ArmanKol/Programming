#som neemt een getallenlijst. de getallenlijst wordt in optellijst opgeteld en vervolgens teruggestuurd.
def som(getallenlijst):
    optellijst = sum(getallenlijst)
    return optellijst

lijst = [1, 3, 7, 4, 3, 6, 8, 2]
print(lijst)

print(som(lijst))

