from flask import Flask
from os import getenv
from app.configs import database, migrations, auth
from app import routes


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    database.init_app(app)
    migrations.init_app(app)
    auth.init_app(app)
    routes.init_app(app)

    return app