from flask_restful import Resource, marshal
from src.model.users import User
from src import db, request
from src.model.schemas.users import users_fields
from flask_bcrypt import Bcrypt
from flask import current_app
from src.repository.user.userRepository import UserRepository
from src.infra.model.resultModel import ResultModel
from src.contract.user.createUserContract import CreateUserContract
from src.contract.user.updateUserContract import UpdateUserContract
from src.contract.user.deleteUserContract import DeleteUserContract
from src.contract.user.getByIdUserContract import GetByIdUserContract


class UserHandler:
    def get_all_users(self):
        user = UserRepository()
        users = user.get_all()
        return users

    def get_by_username(self, username):
        repository = UserRepository()
        user = repository.get_by_username(username)
        return user

    def get_by_id(self, _id):
        contract = GetByIdUserContract()
        if not(contract.validate(_id)):
            return ResultModel('Envie todos parametros obrigatorios.', False, contract.errors).to_dict(), 406
        repository = UserRepository()
        user = repository.get_by_id(_id)
        return user

    def create_user(self):
        contract = CreateUserContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Envie todos parametros obrigatorios.', False, contract.errors).to_dict(), 406
        user = UserRepository()
        new_user = user.create(playload.get('username'), playload.get(
            'password'), playload.get('is_admin'))
        return new_user

    def update_user(self):
        contract = UpdateUserContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Envie todos parametros obrigatorios.', False, contract.errors).to_dict(), 406
        repository = UserRepository()
        user = repository.update(
            playload.get('id'),
            playload.get('username'),
            playload.get('password'),
            playload.get('is_admin'))
        return user

    def delete_user(self):
        contract = DeleteUserContract()
        playload = request.json
        if not(contract.validate(playload)):
            return ResultModel('Envie todos parametros obrigatorios.', False, contract.errors).to_dict(), 406

        repository = UserRepository()
        user = repository.delete(playload.get('id'))
        return user
