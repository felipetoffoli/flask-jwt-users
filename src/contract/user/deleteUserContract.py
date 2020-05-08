from src.infra.model.resultModel import ResultErrorModel


class DeleteUserContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, data):
        _id = data.get('id')

        if not _id:
            self.add_error('id', 'id é obrigatorio.')
        if type(_id) != type(1):
            self.add_error('id', 'id precisa ser um inteiro.')
        return self.valid()
