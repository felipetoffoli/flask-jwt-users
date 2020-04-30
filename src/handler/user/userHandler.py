from flask_restful import Resource, marshal
from src.model.users import User
from src import db, request
from src.model.schemas.users import users_fields
from flask_bcrypt import Bcrypt
from flask import current_app


class UserHandler:

    def get_all_users(self):
        users = User.query.all()
        return marshal(users, users_fields, 'users'), 200

    def create_user(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        is_admin = playload.get('is_admin')
        print(is_admin, type(is_admin))
        user = User(username, password, is_admin)
        db.session.add(user)
        db.session.commit()
        
        return marshal(user, users_fields, 'user'), 201

    def update_user(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        is_admin = playload.get('is_admin')
        _id = playload.get('id')

        user = User.query.get(_id)
        if not user:
            return {'message': 'Usuario não existe'}
        
        bcrypt = Bcrypt(current_app)
        user.username = username
        user.password = bcrypt.generate_password_hash(password)
        user.is_admin = is_admin
        
        db.session.add(user)
        db.session.commit()
        
        return marshal(user, users_fields, 'user'), 200


    def delete_user(self):
        playload = request.json
        _id = playload.get('id')

        user = User.query.get(_id)
        if not user:
            return {'message': 'Usuario não existe'}, 200

        db.session.delete(user)
        db.session.commit()
        
        return marshal(user, users_fields, 'user'), 200