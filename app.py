import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/time")
def server_time():
    return jsonify({"server_time": datetime.now().isoformat()})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
