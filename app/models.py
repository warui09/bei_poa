#!/usr/bin/python3
""" define database models """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash
from .config import Config
from flask_login import UserMixin

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(64), nullable=False, index=True)
    last_name = Column(String(64), nullable=False, index=True)
    email = Column(String(120), nullable=False, unique=True, index=True)
    phone_number = Column(String(13), nullable=False)
    password_hash = Column(String(256), nullable=False)

    products = relationship("Product", back_populates="owner")
    bids = relationship("Bids", back_populates="bidder")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        # Return True if the user is active, False otherwise
        return True

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.email}>"

class Bids(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Integer, nullable=False)
    accepted = Column(Boolean, default=False)
    product_id = Column(Integer, ForeignKey("product.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    product = relationship("Product", back_populates="bids")
    bidder = relationship("User", back_populates="bids")

    def __repr__(self):
        return f"<Bids {self.id} {self.price}>"

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(120), nullable=False, index=True)
    quantity = Column(String(256), nullable=False)
    image_url = Column(String(256))
    place = Column(String(256))
    user_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="products")
    bids = relationship("Bids", back_populates="product")

    def __repr__(self):
        return f"<Product {self.id} {self.product_name} {self.quantity}>"
