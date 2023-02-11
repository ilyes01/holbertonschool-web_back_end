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

# Define a`get_locale`function to determine the best match between the client's
@babel.localeselector
def get_locale():
    """Determines the best match between the client's
    languages and our supported languages"""

    # Use request.accept_languages to get a list of the client's
    return request.accept_languages.best_matches(app.config['LANGUAGES'])
# Define a route for the root URL ('/')
@app.route('/')
def welcome():
    """ render a html file """

    # Render the '1-index.html' template file
    return render_template('2-index.html')

# Check if the script is run as the main program


if __name__ == '__main__':
    """main"""
    # Run the Flask application
    app.run()
