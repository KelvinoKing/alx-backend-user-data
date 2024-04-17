#!/usr/bin/env python3
"""
Create a new Flask view that handles all routes for the Session
authentication.
In the file api/v1/views/session_auth.py, create a route POST
/auth_session/login (= POST /api/v1/auth_session/login):
Slash tolerant (/auth_session/login == /auth_session/login/)
You must use request.form.get() to retrieve email and password
parameters
If email is missing or empty, return the JSON
{ "error": "email missing" } with the status code 400
If password is missing or empty, return the JSON
{ "error": "password missing" } with the status code 400
Retrieve the User instance based on the email - you must
use the class method search of User (same as the one used for the BasicAuth)
If no User found, return the JSON { "error": "no user found for this email" }
with the status code 404
If the password is not the one of the User found, return the JSON
{ "error": "wrong password" } with the status code 401 - you
must use is_valid_password from the User instance
Otherwise, create a Session ID for the User ID:
You must use from api.v1.app import auth - WARNING: please import it
only where you need it - not on top of the file (can generate circular
import - and break first tasks of this project)
You must use auth.create_session(..) for creating a Session ID
Return the dictionary representation of the User - you must use to_json()
method from User
You must set the cookie to the response - you must use the value of the
environment variable SESSION_NAME as cookie name - tip
"""
from flask import jsonify, request
from typing import Tuple
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> Tuple[str, int]:
    """Handles all routes for session authentication"""
    usrEmail = request.form.get('email')
    usrPassword = request.form.get('password')
    if usrEmail is None or len(usrEmail.strip()) == 0:
        return jsonify({"error": "email missing"}), 400
    if usrPassword is None or len(usrPassword.strip()) == 0:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': usrEmail})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) <= 0:
        return jsonify({"error": "no user found for this email"}), 404
    if users[0].is_valid_password(usrPassword):
        from api.v1.app import auth
        sessionID = auth.create_session(getattr(users[0], 'id'))
        data = jsonify(users[0].to_json())
        data.set_cookie(getenv('SESSION_NAME'), sessionID)
        return data
    return jsonify({"error": "wrong password"}), 401
