#!/usr/bin/python3
'''flask application that when queried at /hbnb returns HBNB.'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''This function is triggered when querried at '/' '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''this function is triggered when querried at '/hbnb' '''
    return 'HBNB'


if __name__ == "__main__":
    '''specifies the port and hostip our application is listening to.'''
    app.run(debug=True, port=5000, host='0.0.0.0')
