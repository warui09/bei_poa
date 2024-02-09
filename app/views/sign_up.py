#!/usr/bin/python3
""" display sign up form """

from flask import Blueprint, url_for, render_template, redirect

from ..forms import Sign_up

sign_up_bp = Blueprint("sign_up", __name__)

@sign_up_bp.route("/sign_up", methods=["GET", "POST"], strict_slashes=False)
def sign_up():
    form = Sign_up()
    first_name = form.first_name.data
    last_name = form.last_name.data
