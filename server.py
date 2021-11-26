from flask import Flask,render_template, request, Response, redirect,url_for
import json

app = Flask(__name__)

@app.route("/search", methods = ['GET'])
def search():
    query = request.args.get("searchT")
    k = 10
    result = {}
    ids_prueba = [1463641226280771585, 1463641288796946433]
    for result in ids_prueba:
        
    #get_k_tweets(query,k)
    return 'hola'

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=2000, threaded=True, host=('127.0.0.1'))