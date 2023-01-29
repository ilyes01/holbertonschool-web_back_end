#!/usr/bin/env python3
"""a flask app"""



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """ render a html file """
    return render_template('0-index.html')
