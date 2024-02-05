#!/usr/bin/python3
""" config file for various environments """

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev_environment"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "bei_poa.db")
