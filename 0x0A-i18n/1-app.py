#!/usr/bin/env python3
""" Very simple flask app using babel """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Configuration for babel translation """
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app, default_locale='en', default_timezone='UTC')


@app.route("/")
def holby_welcome():
    """ Renders 0-index.html from templates directory """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
