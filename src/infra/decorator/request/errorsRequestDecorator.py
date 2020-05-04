from src import request
from functools import wraps
from src.infra.model.resultModel import ResultModel


class ErrorsRequestDecorator:

    def body_is_json(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                if not request.data:
                    return ResultModel('Corpo da requisição não encontrado.', False, True, None).to_dict(), 406
                if not request.is_json:
                    return ResultModel('Corpo da requisição Precisa ser json.', False, True, None).to_dict(), 406
                if request.json:
                    return fn(*args, **kwargs)
            except Exception as err:
                return ResultModel('Ocorreu algum erro na tentativa de recuperar os dados da sua request.', False, True, str(err)).to_dict(), 406
        return wrapper
  
  