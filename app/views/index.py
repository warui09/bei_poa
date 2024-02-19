#!/usr/bin/python3
""" display home page, consists of all listed products """

from flask import Blueprint, render_template
from ..models import Product
from .. import db

index_bp = Blueprint("index", __name__, template_folder="../templates")


@index_bp.route("/", strict_slashes=False)
@index_bp.route("/index", strict_slashes=False)
def home_page():
    """get all products, and paginate the results with 20 results per page"""

    products = db.paginate(db.select(Product))

    return render_template("index.html", products=products)
