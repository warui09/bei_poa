#!/usr/bin/python3
"""create and return the flask app"""

from flask import Flask
import os

# other imports


def create_app(test_config=None):
    """create and configure flask app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'mysql'),
            )
    
    if test_config is None:
        # load instance config if it exists and not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load config file if passed in
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
