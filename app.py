from flask import Flask, jsonify
from newscrap import scrape
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/',methods=["GET"])
def home():
    return "Hello World!!\nThis is an API to get anything you serach from twitter\n add /search/< anything you want to search >"


@app.route('/search',methods=["GET"])
def dev_search():
    query = "remote developer jobs hiring"
    scrape(query)

    with open('tweets.json') as json_file:
        data = json.load(json_file)

    return jsonify(data)

@app.route('/search/<string:query>',methods=["GET"])
def search(query):
    scrape(query)

    with open('tweets.json') as json_file:
        data = json.load(json_file)

    return jsonify(data)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
