from flask import Blueprint
from app.controllers.admins_controller import create_admin

bp_admins = Blueprint('bp_admins', __name__, url_prefix='/admin')

bp_admins.post('')(create_admin)