from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def holby_welcome():
    """ Renders 0-index.html from templates directory """
    return render_template('0-index.html')
