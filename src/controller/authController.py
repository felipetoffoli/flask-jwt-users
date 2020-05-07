from flask import Blueprint
from src.handler.auth.login import AuthHandler
from src.infra.decorator.request.errorsRequestDecorator import ErrorsRequestDecorator


controller_auth = Blueprint('controller_auth', __name__)
validity_req = ErrorsRequestDecorator()

@controller_auth.route('/login', methods=['POST'])
@validity_req.body_is_json
def login():
    auth = AuthHandler()
    return auth.post()