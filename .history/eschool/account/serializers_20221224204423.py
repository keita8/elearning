from rest_framework import serializers
from django.conf import settings 
from .models import *

# User = settings.AUTH_USER_MODEL


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = (
            "sex",
            "lastname",
            "firstname",
            "birth_date",
            "phone_number",
            "bio",
        )
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = (
            'lastname',
            'firstname',
            'birth_date',
            'bio'
        )