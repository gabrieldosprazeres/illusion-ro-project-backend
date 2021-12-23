class InvalidTypeAdminError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, name: str, last_name: str, email: str, username: str) -> None:

        keys = [name, last_name, email, username]
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


class InvalidKeyAdminError(Exception):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key != 'name' or key != 'last_name' or key != 'email' or key != 'username' or key != 'password':
                self.message = {
                    'available_keys': [
                    'name',
                    'last_name',
                    'email',
                    'username',
                    'password'
                    ]
                }
        super().__init__(self.message)


class EmailNotFound(Exception):


    def __init__(self, email) -> None:

        self.message = {
            'message': f"email: '{email}' not found"
        }

        super().__init__(self.message)