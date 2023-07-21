import csv

highest_scores = {}
with open("./third_task/scores.csv", "r") as general_score:
    reader = csv.reader(general_score)
    next(reader)

    for row in reader:
        player_name = row[0]
        score = int(row[1])

        if player_name in highest_scores:
            highest_scores[player_name] = max(highest_scores[player_name], score)
        else:
            highest_scores[player_name] = score

sorted_player_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)

with open("fourth_task/highest_scores.csv", "w", newline="") as highest_player_scores:
    writer = csv.writer(highest_player_scores)
    writer.writerow(["Player", "Highest Score"])
    writer.writerows(sorted_player_scores)
