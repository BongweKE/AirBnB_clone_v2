#!/usr/bin/python3
'''Starts a flask web application.
The application listens to port 0.0.0.0 port 5000.
Routes:
     /states_list: HtML page with a list of all states in the DBstorage.
'''
from flask import Flask
from model import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''Displays an HTML page with a list of all states in the DBStorage.
    states are sorted by name.
    '''
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    '''remove the current SQLAlchemy session.'''
    storage.close()


if __name__== "__main__":
    app.run(debug=True, host=0.0.0.0, port=5000)
