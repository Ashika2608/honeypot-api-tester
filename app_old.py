from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    api_key = request.headers.get("x-api-key")

    from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Honeypot API Tester is running"})


    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    return jsonify({"message": "Honeypot API Tester is running"}), 200


import os

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

