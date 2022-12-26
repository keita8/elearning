from rest_framework import serializers
from django.conf import settings 
from .models import *

# User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'


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
    # get_lastname = serializers.SerializerMethodField()
    # get_firstname = serializers.SerializerMethodField()
    # get_birth_date = serializers.SerializerMethodField()
    # get_bio = serializers.SerializerMethodField()
    class Meta:
        model = StudentProfile
        fields = (
            'get_user',
        )
    def get_user(self, obj):
        return obj.user.email
    def get_firstname(self, obj):
        return obj.firstname
    def get_birth_date(self, obj):
        return obj.birth_date
    def get_bio(self, obj):
        return obj.bio