from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

@app.route("/api/news", methods=["GET"])
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route("/api/market", methods=["GET"])
def get_market():
    url = f"https://www.alphavantage.co/query?function=GLOBAL_MARKET_STATUS&apikey={ALPHA_VANTAGE_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

@app.route("/api/sentiment", methods=["GET"])
def get_sentiment():
    url = "https://api.twitter.com/2/tweets/search/recent?query=geopolitics"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
