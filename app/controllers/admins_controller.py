from flask import request, jsonify, current_app
from app.controllers import check_email, check_key_for_admin, check_pattern, check_type_for_admin, check_username, check_email_lead
from app.exceptions.admins_exception import InvalidKeyAdminError, InvalidTypeAdminError, EmailNotFound
from app.exceptions import EmailAlreadyExistsError, UsernameAlreadyExistsError, PatternEmailError
from app.models.admins_model import AdminsModel
from app.models.leads_model import LeadsModel


def get_lead_by_email(email: str):
    
    try:
        lead = check_email_lead(email, LeadsModel)

    except EmailNotFound as error:
        return jsonify(error.message), 404

    return jsonify(lead), 200


def create_admin():
    data = request.get_json()

    try:
        check_key_for_admin(data)
        check_type_for_admin(data)
        check_email(data, AdminsModel)
        check_username(data, AdminsModel)
        check_pattern(data)

        password_to_hash = data.pop("password")

        admin = AdminsModel(**data)

        admin.password = password_to_hash

        current_app.db.session.add(admin)
        current_app.db.session.commit()

    except (
        EmailAlreadyExistsError, 
        UsernameAlreadyExistsError
        ) as error:
        return jsonify(error.message), 409

    except (
        PatternEmailError, 
        InvalidTypeAdminError, 
        InvalidKeyAdminError
        ) as error:
        return jsonify(error.message), 400

    return jsonify(admin), 201