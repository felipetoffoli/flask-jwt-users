from src.model.users import User
from src import db
from flask_bcrypt import Bcrypt
from flask import current_app
from flask_restful import marshal
from src.model.schemas.users import users_fields

class UserRepository:
    
    def get_all(self):
        try:
            users = User.query.all()
            data = marshal(users, users_fields)
            return {'message': 'Pesquisa realizada com sucesso', 'data': data, 'erro': False}
        except Exception as e:
            return {'message': 'Não foi possivel realizar a pesquisa.', 'data': False, 'erro': True, 'Exeption': str(e)}

    def create(self, username, password, is_admin):
        try:
            user = User.query.filter_by(username=username).first()
            if user:
                return {'message': f'Usuario "{username}" já existe.', 'data': False, 'erro': True, 'Exeption': False}
            user = User(username, password, is_admin)
            db.session.add(user)
            db.session.commit()
            data = marshal(user, users_fields)
            return {'message': 'Usuario criado com sucesso', 'data': data, 'erro': False}
        except Exception as e:
            return {'message': 'Não foi possivel criar o usuario.', 'data': False, 'erro': True, 'Exeption': str(e)}
        
    def get_by_id(self, _id):
        try:
            user = User.query.get(_id)
            data =  marshal(user, users_fields)
            return {'message': 'Pesquisa realizada com sucesso', 'data': data, 'erro': False}
        except Exception as e:
            return {'message': 'Não foi possivel realizar a pesquisa.', 'data': False, 'erro': True, 'Exeption': str(e)}

    def update(self, _id, username, password, is_admin):
        try:
            user = User.query.get(_id)
            if not user:
                return {'message': 'Usuario não existe', 'data': False, 'error': True}
            bcrypt = Bcrypt(current_app)
            user.username = username
            user.password = bcrypt.generate_password_hash(password)
            user.is_admin = is_admin
            data = marshal(user, users_fields)
            return {'message': 'Usuario atualizado com sucesso!', 'data': data, 'error': False}
        except Exception as e:
            return {'message': 'Não foi possivel atualizar o usuario.', 'data': False, 'erro': True, 'Exeption': str(e)}

    def delete(self, _id):
        try:
            user = User.query.get(_id)
            if not user:
                return {'message': 'Usuario não existe', 'data': False, 'error': True}
            db.session.delete(user)
            db.session.commit()
            data = marshal(user, users_fields)
            return {'message': 'Usuario deletado com sucesso', 'data': data, 'error': True}
        except Exception as e:
            return {'message': 'Não foi possivel deletar o usuario.', 'data': False, 'erro': True, 'Exeption': str(e)}

