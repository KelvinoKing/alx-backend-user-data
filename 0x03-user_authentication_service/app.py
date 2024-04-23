#!/usr/bin/env python3
"""
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """GET route ("/") that returns a JSON payload
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
