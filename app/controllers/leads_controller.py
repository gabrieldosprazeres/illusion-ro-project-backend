from flask import request, jsonify, current_app
from app.controllers import check_email, check_id, check_key_for_lead, check_pattern, check_phone, check_type_for_lead, check_username
from app.exceptions.leads_exception import IdNotFoundError, InvalidKeyLeadError, InvalidTypeLeadError, PatternPhoneError, PhoneAlreadyExistsError
from app.exceptions import EmailAlreadyExistsError, UsernameAlreadyExistsError, PatternEmailError
from app.models.leads_model import LeadsModel


def get_leads():

    page = request.args.get('page', 1, int)
    per_page = request.args.get('per_page', 10, int)

    leads = LeadsModel.query.order_by(LeadsModel.id).all()

    initial = (page - 1) * per_page
    final = per_page * page
    
    current_page = leads[initial:final]

    return jsonify(current_page), 200


def create_lead():
    data: dict = request.get_json()

    try:
        check_key_for_lead(data)
        check_type_for_lead(data)
        check_email(data, LeadsModel)
        check_phone(data, LeadsModel)
        check_username(data, LeadsModel)
        check_pattern(data)

        lead = LeadsModel(**data)

        current_app.db.session.add(lead)
        current_app.db.session.commit()

    except (
        EmailAlreadyExistsError, 
        PhoneAlreadyExistsError, 
        UsernameAlreadyExistsError
        ) as error:
        return jsonify(error.message), 409

    except (
        InvalidTypeLeadError, 
        PatternPhoneError, 
        PatternEmailError, 
        InvalidKeyLeadError
        ) as error:
        return jsonify(error.message), 400

    return jsonify(lead), 201


def delete_lead(lead_id: int):
    
    try:
        check_id(lead_id, LeadsModel)

        LeadsModel.query.filter_by(id=lead_id).delete()

        current_app.db.session.commit()

    except IdNotFoundError as error:
        return jsonify(error.message), 404
    
    return "", 204