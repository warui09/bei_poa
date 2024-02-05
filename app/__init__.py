#!/usr/bin/python3
""" initialize and set up the app """

from config import Config
from extensions import db
from flask import Flask

def create_app():
    """ app factory, creates and returns the app object """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

return app
