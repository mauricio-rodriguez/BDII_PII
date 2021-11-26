import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def load_books(file_name):
    books = []
    for i in range (6):
        with open("libro"+str(i+1)+".txt") as file:
            words = []
            for line in file:
                words += nltk.word_tokenize(line.lower())
            books.append(words)
            file.close()
    return books
                        
    
def get_stop_list():
    with open('stoplist.txt') as file:
        stoplist = [line.lower().strip() for line in file]
        stoplist += ['.','?','-','\n', ',', ';',':','(',')',"''",'»',
                     '«','``','=', '+', '-', '|', '#', 'x', '/', '@',]
    return stoplist

def tokenize(file_name):
    stemmer = SnowballStemmer('spanish')
    books = load_books(file_name)
    stoplist = get_stop_list()
    results = []
    index = 1
    for array in books:
        for word in array:
             if word not in stoplist:
                temp = stemmer.stem(word)
                if (temp,index) not in results:
                    results.append((temp,index))
        index+=1
    return results
            