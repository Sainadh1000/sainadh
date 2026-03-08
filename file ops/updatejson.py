import json

with open("file ops/newjson.json", "r") as file:
    data = json.load(file)

data["age"] = 26

with open("file ops/newjson.json", "w") as file:
    json.dump(data, file)