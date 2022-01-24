from flask import Flask, jsonify
from newscrap import scrape
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# queries = {'1': 'remote developer hiring', '2': 'remote intern hiring'}

@app.route('/search',methods=["GET"])
def search():
    query = "remote developer hiring"
    scrape(query)

    with open('tweets.json') as json_file:
        data = json.load(json_file)

    return jsonify(data)
    # return jsonify({"1":"@#$","2":"wesdrfa"})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
