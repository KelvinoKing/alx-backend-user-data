#!/usr/bin/env python3
"""
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""
from flask import Flask, jsonify
from auth import Auth
from flask import request

Auth = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """GET route ("/") that returns a JSON payload
    """
    return jsonify({"message": "Bienvenue"})


"""
In this task, you will implement the end-point to register a user.
Define a users function that implements the POST /users route.
The end-point should expect two form data fields: "email" and "password".
If the user does not exist, the end-point should register it and respond
with the following JSON payload:

{"email": "<registered email>", "message": "user created"}

If the user is already registered, catch the exception and
return a JSON payload of the form

{"message": "email already registered"}
and return a 400 status code

Remember that you should only use AUTH in this app.
DB is a lower abstraction that is proxied by Auth.
"""


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """POST /users route that expects two form data fields
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
