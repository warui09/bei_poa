#!/usr/bin/python3
""" display the login form """

from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import current_user, login_user
from ..forms.sign_in import Sign_inForm
from ..models import User
from flask_wtf.csrf import generate_csrf
from wtforms.validators import DataRequired, Email
from email_validator import validate_email, EmailNotValidError

sign_in_bp = Blueprint("auth", __name__, template_folder="../templates")

@sign_in_bp.route("/login", strict_slashes=False, methods=["GET", "POST"])
def sign_in():
    # redirect authenticated user to home page
    if current_user.is_authenticated:
        return redirect(url_for("user_home"))

    form = Sign_inForm()
    if form.validate_on_submit():
        # validate email format using Flask-WTF's Email validator
        if not form.email.data:
            flash("Email is required")
            return redirect(url_for("sign_in"))
        # validate email
        try:
            validate_email(form.email.data)
        except EmailNotValidError:
            flash("Invalid email address")
            return redirect(url_for("sign_in"))

        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for("user_home"))
        else:
            flash("Invalid email or password")

    return render_template("sign_in.html", form=form, csrf_token=generate_csrf())
