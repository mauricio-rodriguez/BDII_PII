from nltk.stem import SnowballStemmer

class index:
    def __init__(self):
        self.inverted_index = {}
        
    def sort(self,tokens):
        first_result = sorted(tokens, key=lambda x: x[0])
        second_result = sorted(first_result,key = lambda x:x[1])
        return second_result

    def build_index(self,sorted_tokens):
        
        for element in sorted_tokens:
            self.inverted_index[element[0]] = []
        
        for element in sorted_tokens:
            self.inverted_index[element[0]].append(element[1])
        
        return self.inverted_index

    def L(self, term):
        stemmer = SnowballStemmer('spanish')
        stem = stemmer.stem(term.lower())
        return self.inverted_index[stem]

    def AND(self, array1, array2):
        intersection = [value for value in array1 if value in array2]
        return intersection

    def OR(self, array1, array2):
        union = list(set(array1) | set(array2))
        return union
        
    def AND_NOT(self,array1, array2):
        difference = [value for value in array1 if value not in array2]
        return difference
    


    
    
