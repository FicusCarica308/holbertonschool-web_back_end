#!/usr/bin/env python3
""" Flask application file """
from flask import Flask, json, jsonify, make_response, request, abort, redirect
from auth import Auth


# authentication
AUTH = Auth()

# Flask app
app = Flask(__name__)


@app.route('/')
def route_endpoint():
    """ Route handler """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ Creates a user if email given doesnt alread exist """

    email = request.form['email']
    password = request.form['password']

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    return jsonify({"email": email, "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Logs in a user if it exists and adds a cookie to the response """
    email = request.form['email']
    password = request.form['password']

    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    resp = make_response({"email": email, "message": "logged in"})
    resp.set_cookie('session_id', session_id)
    return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Logs out a user if it exists """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ returns a user from a session_id """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200

@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def profile():
    """ """
    email = request.form['email']
    
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
