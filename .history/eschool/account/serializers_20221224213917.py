from dataclasses import fields
from rest_framework import serializers
from django.conf import settings 
from .models import *

# User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentProfile
#         fields = (
#             "sex",
#             "lastname",
#             "firstname",
#             "birth_date",
#             "phone_number",
#             "bio",
#         )
    
class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherProfile
        fields = ("firstname", 'lastname')
