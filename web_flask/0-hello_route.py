#!/usr/bin/python3
'''a simple flask application that retrns hello HBNB'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''Display Hello HBNB when queried at root.'''
    return 'Hello HBNB!'


if __name__ == "__main__":
    '''specifing the mode, host and port to run our application on'''
    app.run(debug=True, port=5000, host='0.0.0.0')
