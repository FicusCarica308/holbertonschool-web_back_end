#!/usr/bin/env python3
""" Flask application file """
from flask import Flask, json, jsonify, make_response, request
from auth import Auth


# authentication
AUTH = Auth()

#Flask app
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
    except:
        return jsonify({"message": "email already registered"})
    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
