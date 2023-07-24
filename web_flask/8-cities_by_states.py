#!/usr/bin/python3

'''Starts a Flask web application on host ='0.0.0.0' on port 5000
runs on port 5000.
The application renders the HTML page 8-cities_by_states.html
'''

from flask import Flask
from flask import render_template
from model import storage

app == Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''Display an HTML page with a list of all states and related cities
    cities and states are sorted by name.
    '''
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    '''removes the current SQLAlchemy  session.'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
