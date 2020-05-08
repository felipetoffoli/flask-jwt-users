class ResultModel:

    def __init__(self, message, data, error, exeption=False):
        self.message = message
        self.data = data
        self.error = error
        self.exeption = exeption
    

    def to_dict(self):
        if self.error:
            return {'message': self.message, 'data': self.data, 'error': self.error, 'exeption': self.exeption}
        return {'message': self.message, 'data': self.data, 'error': self.error}
    

class ResultErrorModel:
    
    
    def __init__(self):
        self.errors = []

    def valid(self):
        if len(self.errors):
            return False
        return True
    
    def add_error(self, name, message):
        self.errors.append(self.dict_error(name, message))
    
    def dict_error(self, name, message):
        return dict(name=name, message=message)
        
