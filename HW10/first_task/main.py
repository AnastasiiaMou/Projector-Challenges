import string
import random


def generate_files():
    summary_filename = "summary.txt"
    with open(summary_filename, "w") as summary_file:
        for letter in string.ascii_uppercase:
            filename = f"{letter}.txt"
            number = random.randint(1, 100)

            with open(filename, "w") as file:
                file.write(str(number))

            summary_file.write(f"File: {filename}, Number: {number}\n")


generate_files()