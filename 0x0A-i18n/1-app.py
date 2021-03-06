#!/usr/bin/env python3
""" Very simple flask app using babel """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Configuration for babel translation """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route("/")
def holby_welcome():
    """ Renders 0-index.html from templates directory """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
