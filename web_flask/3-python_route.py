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
    '''this function is triggered when querried at /c/<name>.
    name(str): input querry string.
    replace underscore(_) with whitespace.'''
    text = name.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_print(text='is cool'):
    '''triggered function when querried at /python/<text>.
    text(str): The input variable.If None text = 'is cool'
    replace underscore in the input string with a whitespace.
    '''
    name = text.replace('_', ' ')
    return f"Python {escape(name)}"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
