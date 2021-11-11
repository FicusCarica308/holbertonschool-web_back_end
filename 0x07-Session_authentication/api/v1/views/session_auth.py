#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import environ


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_handler():
    """ handles login route """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if len(users) == 0 or users is None:
        return jsonify({"error": "no user found for this email"})
    for user in users:
        if user.is_valid_password(password) is False:
            return jsonify({"error": "wrong password"}), 401
        else:
            break
    from api.v1.app import auth
    cookie_name = environ.get('SESSION_NAME')
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)
    return response
