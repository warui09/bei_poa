#!/usr/bin/python3
""" sign up form to get the user's details """

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class Sign_up(FlaskForm):
    """sign up form"""

    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    phone_number = StringField("Phone number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign up")
