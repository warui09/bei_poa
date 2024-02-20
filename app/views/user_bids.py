#!/usr/bin/python3
""" display products listed by the current user """

from flask import Blueprint, render_template, request
from ..models import User, Product, Bids
from flask_login import current_user, login_required, LoginManager
from .. import db

user_bids_bp = Blueprint("user_bids", __name__, template_folder="../templates")

@user_bids_bp.route("/user/bids", strict_slashes=False)
#@login.required
def user_bids():
    user = current_user
    user.id = current_user.id

    page = request.args.get("page", 1, type=int)
    products = db.session.query(Product).where(Product.user_id == user.id).paginate(page=page)
    return render_template("user_bids.html", products=products, current_user=current_user)

