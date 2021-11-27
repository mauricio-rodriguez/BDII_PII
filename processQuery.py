import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import json
import numpy as np

from buildInvertedIndex import stemmer

def calculateTfidf(tf, df, N_Tweets):
    return math.log(1 + tf, 10) * math.log(N_Tweets / df, 10)

def getTfIdf(query, invIndex, N_Tweets):
    input = {}
    index = {}

    for token in query:
        if token in invIndex:
            df_val = invIndex[token][0]
            tfidf = calculateTfidf(1, df_val, N_Tweets)
            input[token] = tfidf

        for tweetId in invIndex[token][1]:
            tf = invIndex[token][1][tweetId]
            df = invIndex[token][0]
            tfidf = calculateTfidf(tf, df, N_Tweets)

            if tweetId not in index:
                index[tweetId] = {}
            
            index[tweetId][token] = tfidf

    inputFile = open('data/tfidf_Input.json', 'w')
    json.dump(input, inputFile)
    indexFile = open('data/tfidf_Index.json', 'w')
    json.dump(index, indexFile)

    inputFile.close()
    indexFile.close()

    return input, index

def getNorm(tfidf_Input, tfidf_Index):
    index = {}
    input = 0

    for token in tfidf:
        input += tfidf[token]**

    for tweetID in tfidf:
        index[tweetID] = np.linalg.norm(tfidf[tweetID])

def tokenizeQuery(query):
    query = query.lower()
    query = nltk.word_tokenize(query)

    steemed_tokens = []

    for token in query:
        steemed_tokens.append(stemmer.stem(token))

    return steemed_tokens

