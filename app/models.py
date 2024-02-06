#!/usr/bin/python3
""" define database models """

from . import db
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone_number = Column(String(13), nullable=False)
    password_hash = Column(String(256))

    products = relationship("Product", back_populates="user")
    bids = relationship("Bids", back_populates="user")

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.email}>"


class Bids(db.Model):
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    accepted = Column(Boolean, default=False)
    product_id = Column(Integer, ForeignKey("product.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    product = relationship("Product", back_populates="bids")
    user = relationship("User", back_populates="bids")

    def __repr__(self):
        return f"<Bids {self.id} {self.price}>"


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    product_name = Column(String(120), nullable=False)
    quantity = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="product")

    def __repr__(self):
        return f"<Product {self.id} {self.product_name} {self.quantity}>"


User.products = relationship("Product", back_populates="user")
User.bids = relationship("Bids", back_populates="user")
Bids.user = relationship("User", back_populates="bids")
Bids.product = relationship("Product", back_populates="bids")
