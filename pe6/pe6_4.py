studentencijfers = [[95,92,86], [66,75,54], [89,72,100], [34,0,0]]

def gemiddelde_per_student(studentencijfers):
    res = []
    for row in studentencijfers:
        for items in row:
            res.append(items)
        antw= [sum(res[0:3]) / 3, sum(res[3:6]) / 3, sum(res[6:9]) / 3, sum(res[9:12]) / 3]
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    res = []
    for row in studentencijfers:
        for items in row:
            res.append(items)
        antw = int(sum(res) / len(res))
    return antw
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))