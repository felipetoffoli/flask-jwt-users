from src.model.users import User
from src import db
from flask_bcrypt import Bcrypt
from flask import current_app


class UserRepository:
    
    def get_all(self):
        return User.query.all()

    def create(self, username, password, is_admin):
        user = User(username, password, is_admin)
        db.session.add(user)
        db.session.commit()
        return user

    def get_by_id(self, _id):
        return User.query.get(_id)

    def update(self, _id, username, password, is_admin):
        user = self.get_by_id(_id)
        if not user:
            return {'message': 'Usuario não existe', 'data': False, 'error': True}
        bcrypt = Bcrypt(current_app)
        user.username = username
        user.password = bcrypt.generate_password_hash(password)
        user.is_admin = is_admin
        return {'message': 'Sucesso ao atualizar o usuario!', 'data': user, 'error': False}