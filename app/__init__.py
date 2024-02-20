#!/usr/bin/python3
""" initialize and set up the app """

from flask_bootstrap import Bootstrap5
from .config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize db
db = SQLAlchemy()

def create_app():
    """app factory, creates and returns the app object"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the db with the app
    db.init_app(app)

    # create database
    from .models import User, Bids, Product
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager(app)
    bootstrap = Bootstrap5(app)

    @login_manager.user_loader
    def load_user(user_id):
        # query user object from database
        #return User.query.get(int(user_id))
        return db.session.query(User).get(int(user_id))

    """ import blueprints """
    from .views.sign_in import sign_in_bp
    from .views.sign_up import sign_up_bp
    from .views.index import index_bp
    from .views.user_home import user_home_bp
    from .views.user_products import user_products_bp
    from .views.user_bids import user_bids_bp
    from .views.product_bid import product_bid_bp

    """ register blueprints """
    app.register_blueprint(sign_in_bp)
    app.register_blueprint(sign_up_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(user_home_bp)
    app.register_blueprint(user_products_bp)
    app.register_blueprint(user_bids_bp)
    app.register_blueprint(product_bid_bp)

    return app
