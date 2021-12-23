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