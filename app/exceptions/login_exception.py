class AdminNotFoundError(Exception):

    def __init__(self, username) -> None:

        self.message = {
            "username": f'{username}',
            "message": "Not registered"
        }

        super().__init__(self.message)


class IncorrectPasswordError(Exception):

    def __init__(self) -> None:

        self.message = {
            "message": "Invalid password"
        }

        super().__init__(self.message)


class InvalidKeyLoginError(Exception):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key != 'username' or key != 'password':
                self.message = {
                    'available_keys': [
                    'username',
                    'password'
                    ]
                }
        super().__init__(self.message)


class InvalidTypeLoginError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, username: str, password: str) -> None:

        keys = [username, password]
        for key in keys:
            if type(key) != str:
                if key == username:
                    self.message = {
                        'available field': {
                            'username': 'string'
                        },
                        'field sent': {
                            'username': f'{self.types[type(username)]}'
                        }
                    }
                elif key == password:
                    self.message = {
                        'available field': {
                            'password': 'string'
                        },
                        'field sent': {
                            'password': f'{self.types[type(password)]}'
                        }
                    }

        super().__init__(self.message)