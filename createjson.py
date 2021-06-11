#Создание json файла

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "test": "test2"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:

with open("testwritejsonfile.json","a") as out:
    #for i in y:
      print(y,file=out)

