#!/usr/bin/python3
""" script that starts a Flask web app """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """ Teardown current session """
    storage.close()


@app.route('/states_list')
def states_ls():
    """ function that Display list of all the states """
    states = storage.all(State)
    states_ls = list(states.values())
    return render_template('7-states_list.html', states=states_ls)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
