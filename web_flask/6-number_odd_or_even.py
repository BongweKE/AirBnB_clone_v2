#!/usr/bin/python3
'''flask application that when queried at /hbnb returns HBNB.'''

from flask import Flask
from markupsafe import escape
from flask import render_template

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
    '''this function is triggered when querried at /c/<name>
    name(str): the string of check.'''
    text = name.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_print(text='is cool'):
    '''this function is triggered when querried at /python or at
    /python/<text>
    text(str): The string to be displayed.
    replace underscores with a whitespace'''
    name = text.replace('_', ' ')
    return f"Python {escape(name)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''this function is triggered when querried at /number/<n>
    n(int): The integer of search.'''
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''trigerred function on querry /number_template/<n>
    n(int): The integer of check'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''triggered function when querried at /number_odd_or_even<n>
    n(int): The integer of check if its odd or even.
    6-number_odd_or_even.html will render appropriate output.'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
