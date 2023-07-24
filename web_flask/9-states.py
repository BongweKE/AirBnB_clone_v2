#!/usr/bin/python3

'''Starts a Flask web application on host ='0.0.0.0' on port 5000
runs on port 5000.
The application renders the HTML page 9-states.html
'''

from flask import Flask
from flask import render_template
from model import storage

app == Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    '''Display an HTML page with a list of all states are sorted by name.
    '''
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''Displays HTML page with info about id , if it exists.'''
    for state in storage.all("State").values():
        if state.id == id:
        render_template("9-states.html", state=states)
    render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    '''removes the current SQLAlchemy  session.'''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
