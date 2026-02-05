from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    api_key = request.headers.get("x-api-key")

    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    return jsonify({"message": "Honeypot API Tester is running"}), 200


if __name__ == "__main__":
    app.run()
