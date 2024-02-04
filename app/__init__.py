#!/usr/bin/python3
""" initialize and set up the app """

from extensions import db
from flask import Flask

def create_app():
    """ app factory, creates and returns the app object """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bei_poa.db"
    db.init_app(app)

return app
