from processQuery import queryResult
from buildInvertedIndex import getIndex

indexPath = 'data/invertedIndex.json'
dataPath = 'data/'


[invertedIndex, totalTweets, allTweets] = getIndex(indexPath, dataPath)


textInput = "keiko"
k = 1
retrievalResult = {}

tweets = queryResult(textInput, invertedIndex, totalTweets, int(k))
print(tweets)
for tweet in tweets:
    retrievalResult[tweet[0]] = allTweets[int(tweet[0])]
    print(retrievalResult)

