from flask import Flask,jsonify,request
import csv

all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
unliked_articles = []

app = Flask(__name__)

@app.route("/getarticles")
def getmovie():
    return jsonify({
        "data": all_articles[0],
        "status": "Success"
    })

@app.route("/likedarticles", methods=["POST"])
def likedarticles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "Success"
    }),201

@app.route("/unlikedarticles", methods=["POST"])
def unlikedarticles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        "status": "Success"
    }),201


if __name__ == "__main__":
    app.run()

