#!/usr/bin/python3
""" display products listed by the current user """

from flask import Blueprint, render_template, request
from ..models import User, Product
from flask_login import current_user, login_required, LoginManager
from .. import db

user_products_bp = Blueprint("user_products", __name__, template_folder="../templates")

@user_products_bp.route("/user/products", strict_slashes=False)
#@login.required
def user_products():
    user = current_user
    user.id = current_user.id

    page = request.args.get("page", 1, type=int)
    products = db.session.query(Product).where(Product.user_id == user.id).paginate(page=page)
    product = db.session.query(Product).where(Product.user_id == user.id).first()
    bids = product.bids
    return render_template("user_products.html", products=products, bids=bids, current_user=current_user)
