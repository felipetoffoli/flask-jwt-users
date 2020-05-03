from flask_restful import  marshal
from src.model.users import User
from src.model.schemas.users import users_fields
from src import db, request
from flask_jwt_extended import create_access_token
from flask import current_app
from flask_bcrypt import Bcrypt
import datetime


class AuthHandler:
    
    def post(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        
        if not (username and password):
            return {'message': 'Informe usuario e senha'}

        bcrypt = Bcrypt(current_app)
        print(username, password)
        crypt_password =  bcrypt.generate_password_hash(password)

        user = User.query.filter_by(username=username).first()     
        if not user and bcrypt.check_password_hash(crypt_password, password):
            return {'message': 'Credenciais incorretas'}
        
        data = {
            'id': user.id,
            'username': user.username,
            'is_admin': user.is_admin,
        }
        
        expires = datetime.timedelta(days=30)
        token = create_access_token(identity=user.username, expires_delta=expires, user_claims=data)
        return {'access_token': token}, 201
