import json
from snownlp import SnowNLP

youtuberName = "JoemanStarCraft"
scoreGame = {}
midnum = []
# Opening JSON file
f = open('comments/dailyLive/'+youtuberName + '.json', encoding='utf-8')
dataComment = json.load(f)
f.close()
sum = 0
# Iterating through the json
# list
for i in dataComment:
    s1 = SnowNLP(i)
    print(i, s1.sentiments)
    sum += s1.sentiments

scoreGame[youtuberName] = str(sum/len(dataComment))
print("average is:" + str(sum/len(dataComment)))
print(scoreGame)


fs = open('score/scoreDailylife.json', encoding='utf-8')
data = json.load(fs)
# write

data[youtuberName] = str(sum/len(dataComment))
with open('score/scoreDailylife.json', 'w') as outfile:
    json.dump(data, outfile)


print(data)
print(median_value)
