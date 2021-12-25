from flask import Blueprint
from app.controllers.leads_controller import create_lead, delete_lead, get_leads
from flask_jwt_extended import jwt_required


bp_leads = Blueprint('bp_leads', __name__, url_prefix='/leads')


bp_leads.get('')(jwt_required()(get_leads))
bp_leads.post('')(create_lead)
bp_leads.delete('/<int:lead_id>')(delete_lead)