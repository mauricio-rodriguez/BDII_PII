from flask import Flask,render_template, request, Response, redirect,url_for
import json

test = [
  {
    "id": 1463641226280771585,
    "date": "Wed Nov 24 22:50:36 +0000 2021",
    "text": "b'Manchester City vs. PSG: resultado, resumen y goles del partidazo por la fecha 5 de Champions League - RPP Noticias: * Manchester City vs. PSG: resultado, resumen y goles del partidazo\\xe2\\x80\\xa6 https://t.co/jknNl3FuQT #Videosm\\xc3\\xa1sVistos #ChampionsLeague #LionelMessi #ManchesterCity #PSG https://t.co/dj5Wl2J0po'",
    "user_id": 3100648439,
    "user_name": "@feedsperu",
    "profile_image_url": "https://pbs.twimg.com/profile_images/1455336206732914690/FS6Abdlx_400x400.jpg",
    "location": {},
    "retweeted": False
  },
  {
    "id": 1463641288796946433,
    "date": "Wed Nov 24 22:50:51 +0000 2021",
    "text": "b'@jonytejero231 @CuentaSrFtbol3 @InvictosSomos bueno si tu crees que el united va a remontar al liverpool, chelsea y city en la liga estas bien pendejo'",
    "user_id": 1423460594766712833,
    "user_name": "@10Cesarac",
    "profile_image_url": "https://pbs.twimg.com/profile_images/1458613711141314562/CalC-H76_400x400.jpg",
    "location": {},
    "retweeted": False
  },
  {
    "id": 1463641293960081408,
    "date": "Wed Nov 24 22:50:52 +0000 2021",
    "text": "b'@Ricknaci El amateurismo si se suma. Podes corroborarlo en el sitio oficial de @AFA. Saludos'",
    "user_id": 1280169665050947584,
    "user_name": "@ArchivoFutbolAR",
    "profile_image_url": "https://pbs.twimg.com/profile_images/1334246199642222596/TAtCpeYi_400x400.jpg",
    "location": {},
    "retweeted": False
  },
  {
    "id": 1463641294920638464,
    "date": "Wed Nov 24 22:50:52 +0000 2021",
    "text": "b'RT @LibertadoresBR: \\xf0\\x9f\\x8e\\xa5\\xf0\\x9f\\x94\\xb4\\xe2\\x9a\\xab\\xef\\xb8\\x8f Tem @Flamengo treinando no campo do @OficialCAP! Siga AO VIVO na MEGA LIVE da CONMEBOL #Libertadores direto do Uru\\xe2\\x80\\xa6'",
    "user_id": 55706512,
    "user_name": "@comexsd",
    "profile_image_url": "https://pbs.twimg.com/profile_images/1119898163/DSC00609_400x400.JPG",
    "location": {},
    "retweeted": True,
    "RT_text": "b'\\xf0\\x9f\\x8e\\xa5\\xf0\\x9f\\x94\\xb4\\xe2\\x9a\\xab\\xef\\xb8\\x8f Tem @Flamengo treinando no campo do @OficialCAP! Siga AO VIVO na MEGA LIVE da CONMEBOL #Libertadores direto do Uruguai!  \\xf0\\x9f\\x94\\x97\\xf0\\x9f\\x91\\x89 https://t.co/KjibON20NV https://t.co/rcNdzieOMf'",
    "RT_user_id": 1021446194197925888,
    "RT_user_name": "@LibertadoresBR"
  },
  {
    "id": 1463641297286225925,
    "date": "Wed Nov 24 22:50:53 +0000 2021",
    "text": "b'RT @ERNESTOMorenoG8: La cantante brasile\\xc3\\xb1a Anitta ser\\xc3\\xa1 la encargada del Show de apertura de la Final de la Conmebol Libertadores, que se ju\\xe2\\x80\\xa6'",
    "user_id": 853161817,
    "user_name": "@ChayeneCurica",
    "profile_image_url": "https://pbs.twimg.com/profile_images/1448827605604519941/GVWOGgRa_400x400.jpg",
    "location": {},
    "retweeted": True,
    "RT_text": "b'La cantante brasile\\xc3\\xb1a Anitta ser\\xc3\\xa1 la encargada del Show de apertura de la Final de la Conmebol Libertadores, que se jugar\\xc3\\xa1 este s\\xc3\\xa1bado a las 16 horas en el estadio Centenario de Montevideo entre Palmeiras y Flamengo. https://t.co/UatfILc0yz'",
    "RT_user_id": 1417058832405118978,
    "RT_user_name": "@ERNESTOMorenoG8"
  },
  {
    "id": 1463641301010759689,
    "date": "Wed Nov 24 22:50:53 +0000 2021",
    "text": "b'@BostonMan15 @jmmr_jose @2010MisterChip Si ahora es triste imagina cuando tenga que ver los jueves a su barsa en Europa league jajaja'",
    "user_id": 3034283909,
    "user_name": "@thylarion",
    "profile_image_url": "https://pbs.twimg.com/profile_images/1411960231052156929/vLjdtnmS_400x400.jpg",
    "location": {},
    "retweeted": False
  }]
app = Flask(__name__)

@app.route("/search", methods = ['GET'])
def search():
    query = request.args.get("searchT")
    k = request.args.get("k_closest")
    result = {}
    pruebas = json.dumps(test)
    
    #for result in ids_prueba:
    #get_k_tweets(query,k)
    return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html', tweets = test)


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=3000, threaded=True, host=('127.0.0.1'))