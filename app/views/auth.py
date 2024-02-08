#!/usr/bin/python3
""" display the login form """

from flask import Blueprint, current_app, render_template
from flask_login import current_user, login_user
from .forms import LoginForm

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", strict_slashes=False, methods=["GET", "POST"])
def auth():
    # redirect authenticated user to home page
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))

    form = LoginForm()
    if form.validate.on_submit():
        email = #query db for username and password
        if email is None or not email.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for("auth"))
        login_user(email)
        return redirect(url_for("home_page"))
    return render_template("auth.html", form=form)
