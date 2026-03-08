
import json
data = {
    "name": "John",
    "age": 25,
    "city": "Hyderabad"
}
with open("file ops/newjson.json","w") as file:
    json.dump(data,file)


newdata = {"name":"Alice","age":30}

json_string = json.dumps(newdata)

print(json_string)