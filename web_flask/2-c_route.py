#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ Function that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Function that returns HBNB """
    return "HBNB"


@app.route('/c/<text>')
def C_text(text):
    """ Return 'C ' followed by text from html request """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
