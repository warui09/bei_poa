#!/usr/bin/python3
""" display home page for the app """

from flask import Blueprint, current_app

index_bp = Blueprint("index", __name__)

@index_bp.route("/", strict_slashes=False)
def home_page():
    return "Hello"
