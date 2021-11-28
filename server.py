init = [
  {
    "b'Manchester City vs. PSG: resultado, resumen y goles del partidazo por la fecha 5 de Champions League - RPP Noticias: * Manchester City vs. PSG: resultado, resumen y goles del partidazo\\xe2\\x80\\xa6 https://t.co/jknNl3FuQT #Videosm\\xc3\\xa1sVistos #ChampionsLeague #LionelMessi #ManchesterCity #PSG https://t.co/dj5Wl2J0po'",

  },
  {
    "b'@jonytejero231 @CuentaSrFtbol3 @InvictosSomos bueno si tu crees que el united va a remontar al liverpool, chelsea y city en la liga estas bien pendejo'",


  },
  {


    "b'@Ricknaci El amateurismo si se suma. Podes corroborarlo en el sitio oficial de @AFA. Saludos'",


  },
  {

    "b'RT @LibertadoresBR: \\xf0\\x9f\\x8e\\xa5\\xf0\\x9f\\x94\\xb4\\xe2\\x9a\\xab\\xef\\xb8\\x8f Tem @Flamengo treinando no campo do @OficialCAP! Siga AO VIVO na MEGA LIVE da CONMEBOL #Libertadores direto do Uru\\xe2\\x80\\xa6'",


  },
  {


    "b'RT @ERNESTOMorenoG8: La cantante brasile\\xc3\\xb1a Anitta ser\\xc3\\xa1 la encargada del Show de apertura de la Final de la Conmebol Libertadores, que se ju\\xe2\\x80\\xa6'",


  },
  {

    "b'@BostonMan15 @jmmr_jose @2010MisterChip Si ahora es triste imagina cuando tenga que ver los jueves a su barsa en Europa league jajaja'",

  }]

test = []
app = Flask(__name__)

[invertedIndex, totalTweets, allTweets] = buildIndex(indexPath, dataPath)

@app.route("/search", methods = ['GET'])
def search():
    textInput = request.args.get("searchT")
    k = request.args.get("limit")
    retrievalResult = {}
    result = []

    tweets = query(textInput, int(k), invertedIndex, totalTweets)
    for tweet in tweets:
        retrievalResult[tweet[0]] = allTweets[int(tweet[0])]
        temp = retrievalResult[tweet[0]]
        result.append(temp)

    return render_template('index.html', tweets = result)

@app.route("/")
def index():
    return render_template('index.html', tweets = init)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=3000, threaded=True, host=('127.0.0.1'))