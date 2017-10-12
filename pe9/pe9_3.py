import csv

with open("ScoreGegevens.csv", "r") as Gegevens:
    reader = csv.reader(Gegevens, delimiter=";")
    lijstScores = []
    lijstRijen = []
    for row in reader:
        lijstScores.append(row[2])
        lijstRijen.append(row)
    HoogsteScore = max(lijstScores)
    for rij in lijstRijen:
        if HoogsteScore == rij[2]:
            print("De hoogste score is:",HoogsteScore,"op",rij[1],"behaald door",rij[0])

