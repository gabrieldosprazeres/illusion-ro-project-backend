from app.exceptions.leads_exception import IdNotFoundError, InvalidKeyLeadError, PatternPhoneError, InvalidTypeLeadError, PhoneAlreadyExistsError
from app.exceptions.login_exception import InvalidKeyLoginError, AdminNotFoundError, IncorrectPasswordError, InvalidTypeLoginError
from app.exceptions.admins_exception import EmailNotFound, InvalidKeyAdminError, InvalidTypeAdminError
from app.exceptions import EmailAlreadyExistsError, UsernameAlreadyExistsError, PatternEmailError
from re import fullmatch, compile

def check_email(data: dict, model):

    email = model.query.filter_by(email=data.get('email')).first()

    if email:
        raise EmailAlreadyExistsError(data.get('email'))


def check_phone(data: dict, model):

    phone = model.query.filter_by(phone=data.get('phone')).first()

    if phone:
        raise PhoneAlreadyExistsError(data.get('phone'))


def check_username(data: dict, model):
    
    username = model.query.filter_by(username=data.get('username')).first()
    
    if username:
        raise UsernameAlreadyExistsError(data.get('username'))
    
    
def check_key_for_lead(data: dict):
    
    keys = ['name', 'last_name', 'email', 'phone', 'username']
    
    for key in data.keys():
        if not key in keys or len(data) < 5:
            raise InvalidKeyLeadError(**data)


def check_type_for_lead(data: dict):
    
    for value in data.values():
        if type(value) != str:
            raise InvalidTypeLeadError(**data)


def check_pattern(data: dict):
    pattern_phone = "(\(\d{2}\))(\d{5}\-\d{4})"
    pattern_email = compile("([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        
    email = fullmatch(pattern_email, data.get('email'))
    
    if not email:
        raise PatternEmailError(data)
    
    if 'phone' in data.keys():
        phone = fullmatch(pattern_phone, data.get('phone'))

        if not phone:
            raise PatternPhoneError(data)
    


def check_key_for_admin(data: dict):
    
    keys = ['name', 'last_name', 'email', 'username', 'password']
    
    for key in data.keys():
        if not key in keys or len(data) < 5:
            raise InvalidKeyAdminError(**data)


def check_type_for_admin(data: dict):
    
    for value in data.values():
        if type(value) != str:
            raise InvalidTypeAdminError(**data)


def check_key_for_login(data: dict):
    
    keys = ['username', 'password']
    
    for key in data.keys():
        if not key in keys or len(data) < 2:
            raise InvalidKeyLoginError(**data)


def check_type_for_login(data: dict):
    
    for value in data.values():
        if type(value) != str:
            raise InvalidTypeLoginError(**data)


def check_username_and_password(data: dict, model):
    admin = model.query.filter_by(username=data.get('username')).first()

    if not admin:
        raise AdminNotFoundError(data.get('username'))

    if not admin.check_password(data.get('password')):
        raise IncorrectPasswordError()

    return admin


def check_email_lead(email: str, model):
    
    email_formatted = f'%{email}%'
    
    lead = model.query.filter(model.email.ilike(email_formatted)).all()

    if not lead:
        raise EmailNotFound(email)

    return lead


def check_id(id_to_check, model):

    id = model.query.get(id_to_check)
    
    if not id:
        raise IdNotFoundError