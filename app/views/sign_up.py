#!/usr/bin/python3
""" display sign up form """

from flask import Blueprint, url_for, render_template, redirect, jsonify, request
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash
from ..models import User
from ..forms.sign_up import Sign_up
from flask_wtf.csrf import generate_csrf
from sqlalchemy.exc import IntegrityError
from .. import db


sign_up_bp = Blueprint("sign_up", __name__, template_folder="../templates")


from sqlalchemy.exc import IntegrityError


@sign_up_bp.route(
    "/sign_up",
    methods=["GET", "POST"],
    strict_slashes=False,
)
def sign_up():
    form = Sign_up()
    if request.method == "POST":

        # validate the form
        if form.validate_on_submit():
            # hash the password
            password_hash = generate_password_hash(form.password.data)

            # Check if the email already exists
            existing_user = db.session.query(User).filter_by(email=form.email.data).first()
            if existing_user:
                flash("Email already exists")
                return redirect(url_for("sign_up"))

            # create new User instance
            new_user = User(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    phone_number=form.phone_number.data,
                    password_hash=password_hash,
                )

            db.session.add(new_user)
            db.session.commit()


        # redirect user to index page
        return redirect(url_for("index.home_page"))

    return render_template("sign_up.html", form=form, csrf_token=generate_csrf())
