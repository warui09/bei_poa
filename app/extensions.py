#!/usr/bin/python3
""" central place for all extensions used """

# create and return database object
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """ create base class that inherits from DeclarativeBase """
    pass

db = SQLAlchemy(model_class=Base)
