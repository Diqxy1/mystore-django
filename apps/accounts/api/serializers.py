from django.forms import FileField
from rest_framework import serializers

from ..models import User

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    document = serializers.CharField()
    name = serializers.CharField()
    birth_date = serializers.DateField()
    phone = serializers.CharField()

class DetailUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    document = serializers.CharField()
    name = serializers.CharField()
    birth_date = serializers.DateField()
    phone = serializers.CharField()
    avatar = serializers.FileField()

    class Meta:
        model = User
        fields = [
            'id', 'uuid', 'username', 'user_type', 'avatar',
            'document', 'name', 'birth_date', 'email', 'verified_email',
            'phone', 'verified_phone', 'store_logo', 'virified_upload',
            'manager_password', 'is_active', 'created_at', 'updated_at'
        ]