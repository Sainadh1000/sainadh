import csv

with open("file ops/newcsv.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.seek(0) 
    dictread=csv.DictReader(file)
    for row in dictread:
        print(row)
