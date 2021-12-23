from flask import Blueprint
from app.controllers.admins_controller import create_admin, get_lead_by_email
from flask_jwt_extended import jwt_required


bp_admins = Blueprint('bp_admins', __name__, url_prefix='/admin')

bp_admins.get('/lead/<string:email>')(jwt_required()(get_lead_by_email))
bp_admins.post('')(create_admin)