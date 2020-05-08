from src.infra.model.resultModel import ResultErrorModel


class GetByIdUserContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, _id):
        if not _id:
            self.add_error('id', 'id é obrigatorio.')
        if not _id.isnumeric():
            self.add_error('id', 'id precisa ser um inteiro.')
        return self.valid()
