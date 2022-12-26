from rest_framework import serializers
from .models import *


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
        model = User
        fields = (
            'email',
            'role',
            'is_student',
            'is_teacher',
            
        )