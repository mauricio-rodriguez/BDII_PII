import json
from buildInvertedIndex import getIndex
from processQuery import queryResult

indexPath = 'data/invertedIndex.json'
dataPath = 'tweets/'

test = []

[invertedIndex, totalTweets, allTweets] = getIndex(indexPath, dataPath)


textInput = "messi"
k = 2
retrievalResult = {}
result = []

tweets = queryResult(textInput, invertedIndex, totalTweets, int(k))
for tweet in tweets:
    retrievalResult[tweet[0]] = allTweets[int(tweet[0])]
    temp = retrievalResult[tweet[0]]
    result.append(temp)
