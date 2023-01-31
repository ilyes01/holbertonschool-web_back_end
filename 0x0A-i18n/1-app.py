#!/usr/bin/env python3
"""a flask app"""


from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)

class Config:
    """configclass"""
    LANGUAGE_CODE = ['en','fr']
    TIME_ZONE = 'UTC'
    local = 'en'

app.config.from_object("1-app.Config")
babel = Babel(app)

@app.route('/')
def hello():
    """ render a html file """
    return render_template('1-index.html')
