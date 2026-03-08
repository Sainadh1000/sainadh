import csv

new_row = ["David", 27, "Chennai"]

with open("file ops/newcsv.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)