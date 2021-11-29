# BDII_PII
## Integrantes
- Mauricio Rodriguez
- Renzo Tenazoa
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

### Integración 
El front recibe el los datos y utiliza una función llamada queryResult que le va a devolver los id de los k tweets más cercanos al query.
Luego, se itera por cada id en esta lista de ids de tweets y obtiene el tweet completo de la lista original de tweets limpios. Este resultado lo 
añade a la lista de resultados y finalmente renderiza de nuevo el index.html, teniendo esta vez como lista de tweets a mostrar los que se obtuvieron de la búsqueda.
```
@app.route("/search", methods = ['GET'])
def search():
    textInput = request.args.get("searchT")
    k = request.args.get("limit")
    retrievalResult = {}
    result = []

    tweets = queryResult(textInput, invertedIndex, totalTweets, int(k))
    for tweet in tweets:
        retrievalResult[tweet[0]] = allTweets[int(tweet[0])]
        temp = retrievalResult[tweet[0]]
        result.append(temp)

    return render_template('index.html', tweets = result)
```
En detalle, la función queryResult toneniza el query recibido y seguido de eso obtiene los pesos TFidf de todos los tweets que tengan asociadas las palabras encontradas en el query, luego con estos pesos calcula su *score* utilizando la similutud de coseno. Finalmente, retorna los primeros K elementos de la lista,
o en caso la lista contenga menos de K elementos, los retorna todos.
```
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
```

## Resultados
### Vista principal
La vista principal de la página es simplemente una imagen relacionada al tema que es el fútbol, con el título de 
eliminatorias conmebol

![alt text](https://github.com/mauricio-rodriguez/BDII_PII/blob/main/img_informe/principal.jpg)

### Busqueda de contenido
Deslizando hacia abajo de la vista principal, se observan unos tweets iniciales y 2 inputs de búsqueda, en el que se introduce el texto a buscar
y la cantidad de tweets que se busca recuperar.
En el caso que se muestra, se va a hacer una búsqueda con respecto a la palabra messi, y se busca obtener los 5 primeros elementos más cercanos a la palabra

![alt text](https://github.com/mauricio-rodriguez/BDII_PII/blob/main/img_informe/busqueda%20inicial.jpg)

La imagen inferior muestra el resultado de la búsqueda anterior 
![alt text](https://github.com/mauricio-rodriguez/BDII_PII/blob/main/img_informe/busqueda%20messi.jpg)


