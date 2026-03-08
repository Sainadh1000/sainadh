import json
with open("file ops/newjson.json","r") as file:
    data=json.load(file)
print(data)

json_string = '{"name":"Bob","age":28}'
newdata = json.loads(json_string)
print(newdata)