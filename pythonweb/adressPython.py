import json
  
# Opening JSON file
f = open('data.json',)
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    print(i)
print(len(data))