from flask import Blueprint, jsonify, request
from src.handler.user.userHandler import UserHandler
from flask_jwt_extended import  jwt_required
from flask import current_app
from src.handler.auth.decorator import AuthDecorator

controller_user = Blueprint('controller_user', __name__)
jwt = AuthDecorator()


@controller_user.route('/users', methods=['GET'])
@jwt_required
def get_all():
    user = UserHandler()
    return user.get_all_users()

@controller_user.route('/user', methods=['POST'])
# @jwt.admin_required
def post():
    user = UserHandler()
    return user.create_user()

@controller_user.route('/user', methods=['PUT'])
@jwt.admin_required
def put():
    user = UserHandler()
    return user.update_user()

@controller_user.route('/user', methods=['DELETE'])
@jwt.admin_required
def delete():
    user = UserHandler()
    return user.delete_user()

