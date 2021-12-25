class PhoneAlreadyExistsError(Exception):


    def __init__(self, phone) -> None:

        self.message = {
            'message': f"phone: '{phone}' already exists"
        }

        super().__init__(self.message)


class InvalidTypeLeadError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, name: str, last_name: str, email: str, phone: str, username: str) -> None:

        keys = [name, last_name, email, phone, username]
        for key in keys:
            if type(key) != str:
                if key == name:
                    self.message = {
                        'available field': {
                            'name': 'string'
                        },
                        'field sent': {
                            'name': f'{self.types[type(name)]}'
                        }
                    }
                elif key == last_name:
                    self.message = {
                        'available field': {
                            'last_name': 'string'
                        },
                        'field sent': {
                            'last_name': f'{self.types[type(last_name)]}'
                        }
                    }
                elif key == email:
                    self.message = {
                        'available field': {
                            'email': 'string'
                        },
                        'field sent': {
                            'email': f'{self.types[type(email)]}'
                        }
                    }
                elif key == phone:
                    self.message = {
                        'available field': {
                            'phone': 'string'
                        },
                        'field sent': {
                            'phone': f'{self.types[type(phone)]}'
                        }
                    }
                elif key == username:
                    self.message = {
                        'available field': {
                            'username': 'string'
                        },
                        'field sent': {
                            'username': f'{self.types[type(username)]}'
                        }
                    }

        super().__init__(self.message)


class PatternPhoneError(Exception):
    def __init__(self, data: dict):
        self.message = {
            'field sent': {
                'phone': f"{data.get('phone')}",
                'message': 'default for phone (xx) xxxxx-xxxx'
            }
        }

        super().__init__(self.message)


class InvalidKeyLeadError(Exception):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key != 'name' or key != 'last_name' or key != 'email' or key != 'phone' or key != 'username':
                self.message = {
                    'available_keys': [
                    'name',
                    'last_name',
                    'email',
                    'phone',
                    'username'
                    ]
                }
        super().__init__(self.message)


class IdNotFoundError(Exception):


    def __init__(self) -> None:
        self.message = {
            'message': 'Id not found'
        }
        super().__init__(self.message)

