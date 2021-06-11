#Создание json файла

import json

# создаём объект
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "test": "test2"
}

# конвертируем в JSON:
y = json.dumps(x)

# записываем в файл testwritejsonfile.json

with open("testwritejsonfile.json","a") as out:
    #for i in y:
      print(y,file=out)

