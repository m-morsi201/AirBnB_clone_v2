#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """ Function that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Function that returns HBNB """
    return "HBNB"


@app.route("/c/<text>")
def C_text(text):
    """ Display a text starting with C """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def py_display(text='is_cool'):
    """ display 'Python', followed by the value of the text """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def int_display(n):
    """ display 'n is a number' only if n is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """display HTML is "n" is a number only if n is an integer"""
    return render_template('5-number.html', name=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
