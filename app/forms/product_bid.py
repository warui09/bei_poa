#!/usr/bin/python3
""" product bid form """

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Product_bid(FlaskForm):
    price = StringField("Price", validators=[DataRequired()])
    submit = SubmitField("Submit bid")

