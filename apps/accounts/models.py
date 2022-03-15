import os
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    UserManager
)


def fileLocation(instance, filename):
    return 'mystore_data/{0}/{1}'.format(instance.document, os.path.basename(filename))

class User(AbstractBaseUser, PermissionsMixin):

    class UserType(models.TextChoices):
        USER = 'USER', 'Usuário'
        STORE = 'STORE', 'Lojá'
        MANAGER_STORE = 'MANAGER_STORE', 'Gerente de lojá'
        ADMIN = 'ADMIN', 'Administrador'

    username = models.CharField(max_length=100, unique=True)
    uuid = models.UUIDField()
    user_type = models.CharField(max_length=25, choices=UserType.choices, default=UserType.USER.value)
    avatar = models.FileField(upload_to=fileLocation, null=True)

    # step1
    document = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True)

    # step2
    email = models.EmailField(null=True, unique=True)
    verified_email = models.BooleanField(default=False)
    # step3
    phone = models.CharField(null=True, max_length=20, unique=True)
    verified_phone = models.BooleanField(default=False)

    # step4
    store_logo = models.FileField(upload_to=fileLocation, null=True)
    verified_upload = models.BooleanField(default=False)

    # step5
    # password

    # step6
    manager_password = models.CharField(max_length=255, null=True)

    is_active = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(
        'pertence a administração',
        default=False,
        help_text='Usuário com acesso ao painel gerald e administração',
    )

    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'document'

    REQUIRED_FIELDS = ['name', 'username', 'uuid']

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username


    @property
    def has_password(self):
        return True if self.password else False

    @property
    def has_manager_password(self):
        return True if self.manager_password else False

    @property
    def verified_store_logo(self):
        return self.verified_upload