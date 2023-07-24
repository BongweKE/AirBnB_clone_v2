#!/usr/bin/python3

from flask import Flask
from flask import render_template
from model import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():

if __name__ == "__main__":
    app.run("host=0.0.0.0")
