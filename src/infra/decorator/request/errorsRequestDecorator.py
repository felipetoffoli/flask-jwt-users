from src import request
from functools import wraps


class ErrorsRequestDecorator:

    def body_is_json(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                if not request.data:
                    return {'message': 'Corpo da requisição não encontrado.', 'data': False, 'error': True, 'Exeption': None}, 406
                if not request.is_json:
                    return {'message': 'Corpo da requisição Precisa ser json.', 'data': False, 'error': True, 'Exeption': None}, 406
                if request.json:
                    return fn(*args, **kwargs)
            except Exception as err:
                return {'message': 'Ocorreu algum erro na tentativa de recuperar os dados da sua request. ', 'data': False, 'error': True, 'Exeption': str(err)}, 406
        return wrapper
  
  