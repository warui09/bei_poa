#!/usr/bin/python3
""" display home page for the app """

from flask import Blueprint, current_app

index = Blueprint("index", __name__)

@index.route("/")
def home_page():
    return "Hello"
