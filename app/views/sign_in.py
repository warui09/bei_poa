#!/usr/bin/python3
""" display the login form """

from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash
from ..forms.sign_in import Sign_inForm
from ..models import User
from .. import db
from flask_wtf.csrf import generate_csrf

sign_in_bp = Blueprint("auth", __name__, template_folder="../templates")

@sign_in_bp.route("/login", strict_slashes=False, methods=["GET", "POST"])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for("user_home.user_home"))

    form = Sign_inForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # user = User.query.filter_by(email=email).first()
        user = db.session.query(User).filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Logged in successfully")
            return redirect(url_for("user_home.user_home"))
        else:
            flash("Invalid email or password")

    return render_template("sign_in.html", form=form, csrf_token=generate_csrf())
