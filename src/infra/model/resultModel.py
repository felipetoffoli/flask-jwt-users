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