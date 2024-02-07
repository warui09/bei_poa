#!/usr/bin/python3
""" display the login form """

from app import app

@app.route("/login", strict_slashes=False):
    return "login"
