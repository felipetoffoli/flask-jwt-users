from functools import wraps
from flask_jwt_extended import get_jwt_claims, verify_jwt_in_request

class AuthDecorator:
        
    def admin_required(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            if claims['is_admin'] != True:
                return {'msg': 'Requer permissão do tipo ADMIN', 'error': True, 'data': False}, 403
            else:
                return fn(*args, **kwargs)
        return wrapper