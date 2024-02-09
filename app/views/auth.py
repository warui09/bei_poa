#!/usr/bin/python3
""" display the login form """

from flask import Blueprint, current_app, render_template, redirect, flash
from flask_login import current_user, login_user
from ..forms.login import LoginForm
from ..models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", strict_slashes=False, methods=["GET", "POST"])
def auth():
    return "login"
    """
    # redirect authenticated user to home page
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))

    form = LoginForm()
    if form.validate.on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for("home_page"))
        else:
            flash("Invalid email or password")

    return redirect(url_for("login"))
    """
