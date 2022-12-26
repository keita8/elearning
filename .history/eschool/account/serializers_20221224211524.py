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
    
class StudentSerializer(serializers.ModelSerializer):
    get_user = serializers.SerializerMethodField(read_only=True)
    # get_lastname = serializers.SerializerMethodField()
    # get_firstname = serializers.SerializerMethodField()
    # get_birth_date = serializers.SerializerMethodField()
    # get_bio = serializers.SerializerMethodField()
    class Meta:
        model = TeacherProfile
        fields = ('firstname', 'lastname', 'bio')
    def get_user(self, obj):
        return obj.user.email
    def get_firstname(self, obj):
        return obj.firstname
    def get_birth_date(self, obj):
        return obj.birth_date
    def get_bio(self, obj):
        return obj.bio