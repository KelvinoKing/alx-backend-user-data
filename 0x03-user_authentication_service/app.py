#!/usr/bin/env python3
"""
Create a Flask app that has a single GET route ("/")
and use flask.jsonify to return a JSON payload of the form:
"""
from flask import Flask, jsonify, abort, redirect, Response
from auth import Auth
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from typing import List, Dict, Union, Any, Tuple

Auth = Auth()
app = Flask(__name__)
app.secret_key = "holberton"
# Time for a session to live
app.config.update(SESSION_COOKIE_MAX_AGE=60)


@app.route("/", methods=["GET"], strict_slashes=False)
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


@app.route("/users", methods=["POST"], strict_slashes=False)
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    POST /sessions route that expects two form data fields
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not Auth.valid_login(email, password):
        abort(401)
    session_id = Auth.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """
    DELETE /sessions route that expects a session_id
    """
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)
    user = Auth.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    Auth.destroy_session(user.id)
    return redirect('/')


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """
    GET /profile route that expects a session_id
    """
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)
    user = Auth.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
