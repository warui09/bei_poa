#!/usr/bin/python3
""" display sign up form """

from flask import Blueprint, url_for, render_template, redirect
from werkzeug.security import generate_password_hash
from ..models import User, session
from ..forms.sign_up import Sign_up
from flask_wtf.csrf import generate_csrf

sign_up_bp = Blueprint("sign_up", __name__, template_folder="../templates")


@sign_up_bp.route(
    "/sign_up",
    methods=["GET", "POST"],
    strict_slashes=False,
)
def sign_up():
    form = Sign_up()

    # validate the form
    if form.validate_on_submit():
        # hash the password
        password_hash = generate_password_hash(form.password.data)

        # create new User instance
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            password_hash=password_hash,
        )

        try:
            session.add(new_user)
            session.commit()
        except Exception as e:
            print(e)

        form = Sign_up()

        # redirect user to index page
        return redirect(url_for("index.home_page"))


    return render_template("sign_up.html", form=form, csrf_token=generate_csrf())
