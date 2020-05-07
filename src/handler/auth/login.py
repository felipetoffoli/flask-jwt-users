from flask_restful import  marshal
from src.model.schemas.users import users_fields
from src import db, request
from flask_jwt_extended import create_access_token
from flask import current_app
from flask_bcrypt import Bcrypt
import datetime
from src.infra.model.resultModel import ResultModel
from src.repository.user.userRepository import UserRepository


class AuthHandler:
    
    def post(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        
        if not (username and password):
            return ResultModel('Informe usuario e senha.', False, True).to_dict(), 406

        bcrypt = Bcrypt(current_app)
        print(username, password)
        crypt_password =  bcrypt.generate_password_hash(password).decode('utf8')
        repository = UserRepository()
        user = repository.get_by_username(username, True)['data']
        if not user:
            ResultModel('Usuario não existe.', False, True)
        if not user or not bcrypt.check_password_hash(user['password'], password):
            return ResultModel('Credenciais incorretas.', False, True).to_dict(), 406
        
        data = {
            'id': user['id'],
            'username': user['username'],
            'is_admin': user['is_admin']
        }
        
        expires = datetime.timedelta(days=30)
        token = create_access_token(identity=user['username'], expires_delta=expires, user_claims=data)
        return ResultModel('Sucesso na geração do token.', token, False).to_dict(), 201
