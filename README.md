# BDII_PII
## Integrantes
- 201810642, Mauricio Rodriguez
- 201810    , Renzo Tenazoa
## Recoleccion de tweets
El primer paso para realizar el índice invertido fue recolectar una gran cantidad de tweets con 
una tracklist relacionada a nuestro tema de interés: Las eliminatorias conmebol.
Estos tweets fueron guardados en un json y posteriormente limpiados para obtener solo los datos que nos interesaban sobre el tweet-
## Construcción del índice invertido
### Primera pasada a los tweets
Una vez obtenidos los tweets, se itera a través de todos los tweets y todas las palabras en los tweets, 
para formar un registro de cuales son las palabras útiles y cuáles son stopwords.
Las palabras útiles son guardadas en un índice pero en una versión *stemmeada*, es decir, la raíz de la palabra con  
`stemmer.stem(word)`
Cabe recalcar que se evitan duplicados al guardar estas versiones *steemeadas*.
 ```
 def preprocess(path = 'data/'):
    ...
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
 ```
En el código se observa que se iteran los tweets y, en caso no sean retwitteados, se inserta la palabra *stemmeada*. Finalmente,
esta lista de palabras *stemmeada* de los tweets se pasa retorna como un set, de forma que no hayan duplicados
### Segunda pasada a los tweets
Obtenidas las palabras stemmeadas se vuelve a iterar a través de todas las palabras en los tweets para obtener en cuáles 
tweets se encuentran estas palabras y cuál es la frecuencia con la que aparecen. Así se obtiene un índice invertido que 
es almacenado en memoria secundaria en un archivo .json
```
def build_index(path = 'data/'):
    ...
    invIndex = {}
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
```
En la función se observa que se genera un diccionario y por cada palabra *stemmeada* se asigna una frecuencia inicial con valor de 0 y un subdiccionario interno vacio, en este subdiccionario van los id de los tweets relacionados a la palabra. Cada vez que la palabra se encuentre dentro de un tweet aumenta su frecuencia y se añade el id del tweet dentro del subdiccionario. Finalmente, el diccionario total es lo que se retorna y este sería el índice invertido. Este diccionario es posteriormente guardado en memoria secundaria en formato .json
## Front y Back
### Front
Respecto al apartado Front, no se utilizó ningún framework o librería en específico.
Se trabajó con html, css  y js puro.

### Back
Respecto al Back, se utilizó el framework flask para python dada su simplicidad.
Asimismo, para mostrar los elementos retornados por el back 
se utilizó la sintaxis de **jinja2**
