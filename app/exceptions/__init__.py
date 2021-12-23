class EmailAlreadyExistsError(Exception):


    def __init__(self, email) -> None:

        self.message = {
            'message': f"email: '{email}' already exists"
        }

        super().__init__(self.message)


class UsernameAlreadyExistsError(Exception):


    def __init__(self, username) -> None:

        self.message = {
            'message': f"username: '{username}' already exists"
        }

        super().__init__(self.message)


class PatternEmailError(Exception):
    def __init__(self, data: dict):
        self.message = {
            'field sent': {
                'email': f"{data.get('email')}",
                'message': 'default for email xxxxx@xxxx.xxx or xxxxx@xxxx.xxx.xx'
            }
        }

        super().__init__(self.message)