#!/usr/bin/python3
""" login form """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class Sign_inForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Login")
