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
### Segunda pasada a los tweets
Obtenidas las palabras stemmeadas se vuelve a iterar a través de todas las palabras en los tweets para obtener en cuáles 
tweets se encuentran estas palabras y cuál es la frecuencia con la que aparecen. Así se obtiene un índice invertido que 
es almacenado en memoria secundaria en un archivo .json
## Front y Back
### Front
Respecto al apartado Front, no se utilizó ningún framework o librería en específico.
Se trabajó con html, css  y js puro.

### Back
Respecto al Back, se utilizó el framework flask para python dada su simplicidad.
Asimismo, para mostrar los elementos retornados por el back 
se utilizó la sintaxis de **jinja2**
