from flask import Blueprint, jsonify, request
from src.handler.auth.login import AuthHandler


controller_auth = Blueprint('controller_auth', __name__)

@controller_auth.route('/login', methods=['POST'])
def login():
    auth = AuthHandler()
    return auth.post()