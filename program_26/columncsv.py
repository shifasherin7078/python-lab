

import csv

filename = "data.csv"

with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], row[2])