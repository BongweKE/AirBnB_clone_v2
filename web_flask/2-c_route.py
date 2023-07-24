#!/usr/bin/python3
'''flask application that when queried at /hbnb returns HBNB.'''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''This function is triggered when querried at '/' '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''this function is triggered when querried at '/hbnb' '''
    return 'HBNB'


@app.route('/c/<name>', strict_slashes=False)
def print_c(name):
    '''function triggered when /c/<name> is querried.
    name is the variable of display.
    replace '_' with ' '.'''
    text = name.replace('_', ' ')
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
