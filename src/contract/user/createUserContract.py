from src.infra.model.resultModel import ResultErrorModel


class CreateUserContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if not username:
            self.add_error('username', 'username é obrigatorio.')
        if username and type(username) != type(''):
            self.add_error('username', 'username precisa ser uma string.')
        if type(data.get('is_admin')) != type(True):
            self.add_error('is_admin', 'is_admin é obrigatorio.')
        if not password:
            self.add_error('password', 'password é obrigatorio.')
        if password and type(password) != type(''):
            self.add_error('password', 'password precisa ser uma string.')
        
        return self.valid()
