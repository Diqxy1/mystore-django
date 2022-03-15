from rest_framework.exceptions import APIException

class BadRequest(APIException):
    status_code = 400
    default_detail = 'Falha na requisição'
    default_code = 'bad_request'


class Forbidden(APIException):
    status_code = 403
    default_detail = 'ação não permitida'
    default_code = 'forbidden'


class NotFound(APIException):
    status_code = 404
    default_detail = 'não encontrado'
    default_code = 'not_found'


class ValidationError(APIException):
    def __init__(self, errors):
        if type(errors) == list:
            self.detail = {'detail': errors}
        else:
            self.detail = {'detail': [errors]}

    status_code = 422
    default_detail = 'erro de validação'
    default_code = 'validation_error'