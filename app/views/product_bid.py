#!/usr/bin/python3
""" display form to submit bid on a product """

from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_user
from ..forms.product_bid import Product_bid
from ..models import User, Bids, Product
from .. import db
from flask_wtf.csrf import generate_csrf

product_bid_bp = Blueprint("Product_bid", __name__, template_folder="../templates")

@product_bid_bp.route("/product/bid<int:product_id>", strict_slashes=False, methods=["GET", "POST"])
def bid(product_id):
    form = Product_bid()
    product = db.session.query(Product).get(product_id)

    # validate the form
    if form.validate_on_submit():
        #create new bid
        new_bid = Bids (
                price = form.price.data,
                product_id = product_id,
                user_id = current_user.id,
            )

        db.session.add(new_bid)
        db.session.commit()

        flash("Bid submitted successfully")
        return redirect(url_for("index.home_page"))

    if request.method == "POST":
        # Handle accepting a bid
        bid_id = request.form.get("bid_id")
        bid = Bids.query.get(bid_id)
        bid.accepted = True
        db.session.commit()
        flash("Bid accepted successfully")


    return render_template("product_bid.html", form=form, product=product)
