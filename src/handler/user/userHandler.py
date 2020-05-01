from flask_restful import Resource, marshal
from src.model.users import User
from src import db, request
from src.model.schemas.users import users_fields
from flask_bcrypt import Bcrypt
from flask import current_app
from src.repository.user.userRepository import UserRepository


class UserHandler:

    def get_all_users(self):
        user = UserRepository()
        users = user.get_all()
        return users


    def create_user(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        is_admin = playload.get('is_admin')

        user = UserRepository()
        new_user = user.create(username, password, is_admin)
        return new_user

    def update_user(self):
        playload = request.json
        username = playload.get('username')
        password = playload.get('password')
        is_admin = playload.get('is_admin')
        _id = playload.get('id')
        
        repository = UserRepository()
        user = repository.update(_id, username, password, is_admin)
        return user


    def delete_user(self):
        playload = request.json
        _id = playload.get('id')

        repository = UserRepository()
        user = repository.delete(_id)
        return user