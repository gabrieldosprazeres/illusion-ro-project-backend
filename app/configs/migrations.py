from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.leads_model import LeadsModel
    from app.models.admins_model import AdminsModel

    Migrate(app, app.db)