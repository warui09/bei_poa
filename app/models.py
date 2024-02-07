#!/usr/bin/python3
""" define database models """

from . import db
from .config import Config
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, backref


class User(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone_number = Column(String(13), nullable=False)
    password_hash = Column(String(256))

    products = relationship("Product", backref="user")
    bids = relationship("Bids", backref="user")

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.email}>"


class Bids(db.Model):
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    accepted = Column(Boolean, default=False)
    product_id = Column(Integer, ForeignKey("product.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    product = relationship("Product", backref="bids")
    user = relationship("User", backref="bids")

    def __repr__(self):
        return f"<Bids {self.id} {self.price}>"


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    product_name = Column(String(120), nullable=False)
    quantity = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", backref="product")

    def __repr__(self):
        return f"<Product {self.id} {self.product_name} {self.quantity}>"

""" persist the tables """
with app.app_context():
    db.create_all
