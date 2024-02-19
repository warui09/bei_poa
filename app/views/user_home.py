#!/usr/bin/python3
""" display user's home page, it lists products that the user has listed
and the bids they have placed """

from flask import Blueprint, render_template, request
from ..models import User, Product
from flask_login import current_user, login_required, LoginManager
from .. import db

user_home_bp = Blueprint("user_home", __name__, template_folder="../templates")

@user_home_bp.route("/user", strict_slashes=False)
@user_home_bp.route("/user/home", strict_slashes=False)
#@login.required
def user_home():
    user = current_user
    user.id = current_user.id

    page = request.args.get("page", 1, type=int)
    products = db.session.query(Product).paginate(page=page)
    return render_template("user_home.html", products=products, current_user=current_user)

