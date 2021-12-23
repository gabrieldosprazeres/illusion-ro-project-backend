from app.exceptions.leads_exception import InvalidKeyLeadError, PatternPhoneError, InvalidTypeLeadError, PhoneAlreadyExistsError
from app.exceptions.admins_exception import InvalidKeyAdminError, InvalidTypeAdminError
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
    pattern_phone = "(\(\d{2}\))(\s)(\d{5}\-\d{4})"
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