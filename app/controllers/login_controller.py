from flask import request, jsonify
from app.controllers import check_key_for_login, check_username_and_password, check_type_for_login
from app.exceptions.login_exception import AdminNotFoundError, IncorrectPasswordError, InvalidKeyLoginError, InvalidTypeLoginError
from app.models.admins_model import AdminsModel
from flask_jwt_extended import create_access_token


def signin():

    data: dict = request.get_json()

    try:
        check_key_for_login(data)
        check_type_for_login(data)

        admin = check_username_and_password(data, AdminsModel)

        access_token = create_access_token(admin)

    except AdminNotFoundError as error:
        return jsonify(error.message), 404

    except IncorrectPasswordError as error:
        return jsonify(error.message), 401

    except (
        InvalidKeyLoginError, 
        InvalidTypeLoginError
        ) as error:
        return jsonify(error.message), 400

    return {"access_token": access_token}, 200