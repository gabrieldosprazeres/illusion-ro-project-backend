from app.exceptions.leads_exception import EmailAlreadyExistsError, InvalidKeyError, PatternEmailError, PatternPhoneError, PhoneAlreadyExistsError, UsernameAlreadyExistsError, InvalidTypeError
from app.models.leads_model import LeadsModel
from re import fullmatch, compile

def check_email(data: dict):

    email = LeadsModel.query.filter_by(email=data.get('email')).first()

    if email:
        raise EmailAlreadyExistsError(data.get('email'))


def check_phone(data: dict):

    phone = LeadsModel.query.filter_by(phone=data.get('phone')).first()

    if phone:
        raise PhoneAlreadyExistsError(data.get('phone'))


def check_username(data: dict):
    
    username = LeadsModel.query.filter_by(username=data.get('username')).first()
    
    if username:
        raise UsernameAlreadyExistsError(data.get('username'))
    
    
def check_type(data: dict):
    
    for value in data.values():
        if type(value) != str:
            raise InvalidTypeError(**data)


def check_pattern(data: dict):
    pattern_phone = "(\(\d{2}\))(\s)(\d{5}\-\d{4})"
    pattern_email = compile("([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    phone = fullmatch(pattern_phone, data.get('phone'))

    if not phone:
        raise PatternPhoneError(data)
    
    email = fullmatch(pattern_email, data.get('email'))
    
    if not email:
        raise PatternEmailError(data)


def check_key(data: dict):
    
    keys = ['name', 'last_name', 'email', 'phone', 'username']
    
    for key in data.keys():
        if not key in keys:
            raise InvalidKeyError(**data)
