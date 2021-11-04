#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, json, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Authentication portion of code ==============================
auth = None
excluded_paths = ['/api/v1/status/',
                  '/api/v1/unauthorized/',
                  '/api/v1/forbidden/']

auth_type = os.environ.get('AUTH_TYPE')

if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import Basic_Auth
    auth = Basic_Auth()

@app.before_request
def before_request_handler():
    """[summary]
    """
    if auth is None:
        return
    if auth.require_auth(request.path, excluded_paths) is False:
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user() is None:
        abort(403)
    print("before_request is running!")
# Authentication portion of code ================================


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_user(error) -> str:
    """ Unathorized user error handler
        (raises a 401)
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def auth_user_forbidden(error) -> str:
    """ Error handler for authorized user that doesnt
        have access to a forbidden resource
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
