from flask import Blueprint
from app.controllers.login_controller import signin

bp_login = Blueprint('bp_login', __name__, url_prefix='/login')

bp_login.post('')(signin)