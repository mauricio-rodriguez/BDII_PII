import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


def get_stop_list():
    with open('stoplist.txt') as file:
        stoplist = [line.lower().strip() for line in file]
        stoplist += ['.','?','-','\n', ',', ';',':','(',')',"''",'»',
                     '«','``','=', '+', '-', '|', '#', 'x', '/', '@',]
    return stoplist

def tokenize(query):
    stemmer = SnowballStemmer('spanish')
    tokens = nltk.word_tokenize(query.lower())
    stoplist = get_stop_list()
    results = []
    
    for word in tokens:
        if word not in stoplist:
            results.append(stemmer.stem(word))
    
    return results

def get_k_tweets(query, k):
    tokens = tokenize(query)
    