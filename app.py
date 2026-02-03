from flask import Flask, request, jsonify
import requests
from config import HEADERS

app = Flask(__name__)

@app.route("/")
def home():
    return "Agentic Honeypot API Tester is Live 🚀"

@app.route("/test", methods=["POST"])
def test_api():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        return jsonify({
            "status_code": response.status_code,
            "response_body": response.json()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
