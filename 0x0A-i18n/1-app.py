#!/usr/bin/env python3
""" flask app"""

# Import the required modules from the Flask library
from flask import Flask, render_template, request, g

# Import the Babel module from the flask_babel library
from flask_babel import Babel

# Create a Flask application instance
app = Flask(__name__)

# Define a Config class for the Babel object
class Config(object):
    """ Config class """

    # List of supported languages
    LANGUAGES = ["en", "fr"]

    # Default language
    BABEL_DEFAULT_LOCALE = "en"

    # Default timezone
    BABEL_DEFAULT_TIMEZONE = "UTC"

# Apply the Config object as the configuration for the Flask application
app.config.from_object(Config)

# Create a Babel object and initialize it with the Flask application
babel = Babel(app)

# Define a route for the root URL ('/')
@app.route('/')
def welcome():
    """ render for html file """

    # Render the '1-index.html' template file
    return render_template('1-index.html')

# Check if the script is run as the main program (as opposed to being imported as a module)
if __name__ == '__main__':
    # Run the Flask application
    app.run()
