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
        model = Stud
        fields = (
            'email',
            'is_student',
            'is_teacher',
            'is_staff',
            'is_admin',
            'is_active',
            'last_login',
            'date_joined'
        )