#!/usr/bin/env python3
"""a flask app"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config(object):
    """configclass"""
    LANGUAGES = ['en','fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCAL = 'en'


app.config.from_object("Config")
babel = Babel(app)


@app.route('/')
def hello():
    """ render a html file """
    return render_template('1-index.html')
