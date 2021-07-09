import json
from snownlp import SnowNLP
# Opening JSON file
f = open('commnet.json', encoding='utf-8')
data = json.load(f)
sum = 0
# Iterating through the json
# list
for i in data:
    s1 = SnowNLP(i)
    print(i, s1.sentiments)
    sum += s1.sentiments
print("average is:" + str(sum/len(data)))
