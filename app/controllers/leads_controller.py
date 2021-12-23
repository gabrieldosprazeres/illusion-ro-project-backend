from flask import request, jsonify, current_app
from app.controllers import check_email, check_key, check_pattern, check_phone, check_type, check_username
from app.exceptions.leads_exception import EmailAlreadyExistsError, InvalidKeyError, InvalidTypeError, PatternEmailError, PatternPhoneError, PhoneAlreadyExistsError, UsernameAlreadyExistsError
from app.models.leads_model import LeadsModel


def get_leads():

    leads = LeadsModel.query.all()

    return jsonify(leads), 200


def create_lead():
    data: dict = request.get_json()

    try:
        check_key(data)
        check_type(data)
        check_email(data)
        check_phone(data)
        check_username(data)
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
        InvalidTypeError, 
        PatternPhoneError, 
        PatternEmailError, 
        InvalidKeyError
        ) as error:
        return jsonify(error.message), 400

    return jsonify(lead), 201

