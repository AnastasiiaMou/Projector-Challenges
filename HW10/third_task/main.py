import csv
import random

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
result = []

for player in players:
    for round in range(100):
        score = random.randint(0, 1000)
        result.append((player, score))


with open("third_task/scores.csv", "w", newline="") as scores:
    writer = csv.writer(scores)
    writer.writerow(["Player", "Score"])
    writer.writerows(result)
