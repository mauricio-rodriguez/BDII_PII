from index import index
import preprocesamiento

if __name__ == "__main__":
    tokens = preprocesamiento.tokenize("libro")
    inverted_index = index()
    inverted_index.build_index(inverted_index.sort(tokens))
    #prueba 1 
    print(inverted_index.L("comienzo"))
    #prueba 2
    print(inverted_index.AND(inverted_index.L("Comarca"),inverted_index.L("Frodo")))
    #prueba 3
    print(inverted_index.AND_NOT(inverted_index.L("Gandalf"),inverted_index.L("Tirith")))
   