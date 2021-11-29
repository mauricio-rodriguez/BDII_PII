import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import json
import numpy as np
import math

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

    for token in tfidf_Input:
        input += tfidf_Input[token]** 2
    
    input = input ** 0.5

    for tweetID in tfidf_Index:
        temp = 0
        for token in tfidf_Index[tweetID]:
            temp += tfidf_Index[tweetID][token] ** 2
        
        index[tweetID] = temp ** 0.5
    
    return input, index

def tokenizeQuery(query):
    query = query.lower()
    query = nltk.word_tokenize(query)

    steemed_tokens = []

    for token in query:
        steemed_tokens.append(stemmer.stem(token))

    return steemed_tokens


def queryResult(query, invIndex, N_Tweets, K):
    query = tokenizeQuery(query)
    tfidf_Input, tfidf_Index = getTfIdf(query, invIndex, N_Tweets)
    scoreCoseno = similitudCoseno(tfidf_Input, tfidf_Index)
    tweets = scoreCoseno.items()

    if len(scoreCoseno) > K:
        k_tweets = list(tweets)[:K]
    else:
        k_tweets = list(tweets)[:]
    
    return k_tweets

def similitudCoseno(tfidf_Input, tfidf_Index):
    score = {}
    norm_Input, norm_Index = getNorm(tfidf_Input, tfidf_Index)


    for tweetID in tfidf_Index:
        dot = 0
        NormaT = norm_Index[tweetID] * norm_Input
        for token in tfidf_Index[tweetID]:
            dot += tfidf_Input[token] * tfidf_Index[tweetID][token]
        
        score[tweetID] = dot / NormaT
    
    score = {k: v for k, v in sorted(score.items(), key=lambda item: item[1])}

    return score




