def kwadraten_som(grondgetallen):
    lijst = []
    for cijfers in range (len(grondgetallen)):
        if grondgetallen[cijfers] >=0:
            lijst.append(grondgetallen[cijfers]**2)
    return sum(lijst)

lijst1 = [4, 5, 3, -81]
print(kwadraten_som(lijst1))
