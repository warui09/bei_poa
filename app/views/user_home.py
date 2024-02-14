#!/usr/bin/python3
""" display user's home page, it lists products that the user has listed
and the bids they have placed """

from flask import Blueprint, render_template
from ..models import User, Product, Bids
from flask_login import current_user
from .. import db

user_home_bp = Blueprint("user_home", __name__, template_folder="../templates")

@user_home_bp.route("/user", strict_slashes=False)
@user_home_bp.route("/user/home", strict_slashes=False)
#@login.required
def user_home():
    user.id = current_user.id
    return user.first_name 
