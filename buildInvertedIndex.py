import os
import json
import nltk
import math 
import numpy as np
from decimal import Decimal
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

def stop_list():
    with open('stoplist.txt') as file:
        stoplist = [line.lower().strip() for line in file]
        stoplist += ['.','?','-','\n', ',', ';',':','(',')',"''",'»',
                     '«','``','=', '+', '-', '|', '#', 'x', '/', '@',
                     '😆', '👍','👍🏻', '🏡','/…','--','RT','`']
    return stoplist

def get_stop_list():
    stop_1 = stop_list()
    stop_2 = stopwords.words("spanish")
    result = list(set(stop_1) | set(stop_2))
    return result

#stop_list = get_stop_list()
def stemmer(text):
    tokens = nltk.word_tokenize(text)
    cleanTokens = tokens.copy()
    


    for token in tokens:
        if token in stop_list:
            cleanTokens.remove(token)   

    for i, _ in enumerate(cleanTokens):
        cleanTokens[i] = stemmer.stem(cleanTokens[i])
        
    return cleanTokens


stemmer = SnowballStemmer("spanish")

def preprocess(path = 'data/'):
    data = os.listdir(path)
    data = open(path + data[0],'r')
    stopList = get_stop_list()

    tweets = json.load(data)
    results = []

    for tweet in tweets:
        if tweet['retweeted'] is False:
            tweetText = tweet['text'].lower()
            tokens = nltk.word_tokenize(tweetText)

            for token in tokens:
                #print(token)
                if token not in stopList:
                    results.append(stemmer.stem(token))
    
    data.close()
    return set(results)

def build_index(path = 'data/'):
    steemed_words = preprocess(path)
    data = os.listdir(path)
    data = open(path + data[0],'r')
    invIndex = {}

    tweets = json.load(data)

    for token in steemed_words:
        invIndex[token] = [0, {}]

    for tweet in tweets:
        if tweet['retweeted'] is False:
            tweetId = tweet['id']
            tweetText = tweet['text'].lower()

            tokens = nltk.word_tokenize(tweetText)

            for token in tokens:
                steemedToken = stemmer.stem(token)
                
                if steemedToken in steemed_words:
                    if tweetId not in invIndex[steemedToken][1]:
                        invIndex[steemedToken][0] +=1
                        invIndex[steemedToken][1][tweetId] = 1
                    else:
                        invIndex[steemedToken][1][tweetId] += 1

    data.close()

    return invIndex

def index_to_json_file(path = 'data/'):
    index = build_index()

    indexFile = open(path, 'w')
    json.dump(index, indexFile)
    indexFile.close()

indexPath = 'data/invertedIndex.json'
dataPath = 'data/'

index_to_json_file(indexPath)