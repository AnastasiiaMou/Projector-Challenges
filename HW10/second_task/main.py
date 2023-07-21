with open("second_task/content.txt", "r") as f1, open(
    "second_task/upper_content.txt", "w"
) as f2:
    for line in f1:
        f2.write(line.upper())
