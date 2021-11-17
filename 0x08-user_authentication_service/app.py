#!/usr/bin/env python3
""" Flask application file """
from flask import Flask, json, jsonify, make_response, request, abort
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

@app.route('/sessions', methods=['POST'])
def login():
    """ Logs in a user if it exists """
    email = request.form['email']
    password = request.form['password']
    
    if AUTH.valid_login(email, password) is False:
        abort(401)
    session_id = AUTH.create_session(email)
    resp = make_response()
    resp.set_cookie('session_id', session_id)
    return jsonify({"email": email, "message": "logged in"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
