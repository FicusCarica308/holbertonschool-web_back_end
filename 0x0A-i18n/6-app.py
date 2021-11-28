#!/usr/bin/env python3
""" Very simple flask app using babel """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config():
    """ Configuration for babel translation """
    LANGUAGES = ["en", "fr"]


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)


@app.before_request
def before_request_handler():
    """ Before request """
    user = get_user()
    g.user = user


def get_user():
    """ Gets a user based on url argument"""
    id = request.args.get('login_as')
    if id is None:
        return None
    try:
        return users.get(int(id))
    except ValueError:
        return None


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    lang = request.args.get('locale')
    user = get_user()
    if user is not None and user.locale in app.config['LANGUAGES']:
        return user.locale
    if lang is not None:
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def holby_welcome():
    """ Renders 0-index.html from templates directory """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
