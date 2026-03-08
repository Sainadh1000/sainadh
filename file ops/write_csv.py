import csv

data = [
    ["Name", "Age", "City"],
    ["John", 25, "Hyderabad"],
    ["Alice", 30, "Mumbai"],
    ["Bob", 28, "Delhi"]
]

with open("file ops/newcsv.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)




newdata = [
    {"Name":"John","Age":25,"City":"Hyderabad"},
    {"Name":"Alice","Age":30,"City":"Mumbai"}
]

with open("file ops/newdata.csv", "w", newline="") as file:
    fieldnames = ["Name","Age","City"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(newdata)
    