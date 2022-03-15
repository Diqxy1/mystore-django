from uuid import uuid4

from apps.accounts.models import User

from apps.shared.exceptions import *

class CreateUserService:

    def __init__(self, serializer_data):
        self._serializer_data = serializer_data
    
    def execute(self):

        self._validations(
            self._serializer_data['username'], 
            self._serializer_data['document'],
            self._serializer_data['email'],
            self._serializer_data['phone']
        )

        user = self._create()
        
        return user

    def _validations(self, username: str, document: str, email: str, phone: str):
        username_exist = User.objects.filter(username = username).exists()

        if username_exist:
            raise BadRequest(detail='Username já cadastrado')

        document_exist = User.objects.filter(document = document).exists()
        
        if document_exist:
            raise BadRequest(detail='Documento já cadastrado')

        email_exist = User.objects.filter(email = email).exists()

        if email_exist:
            raise BadRequest(detail='Email já cadastrado')
        
        phone_exist = User.objects.filter(phone = phone).exists()

        if phone_exist:
            raise BadRequest(detail='Telefone já cadastrado')
    
    def _create(self):
        user = User.objects.create(
            **self._serializer_data,
            uuid=uuid4()
        )
        return user