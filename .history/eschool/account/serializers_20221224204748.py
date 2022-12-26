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
    get_lastname = serializers.SerializerMethodField()
    get_firstname = serializers.SerializerMethodField()
    get_birth_date = serializers.SerializerMethodField()
    get_bio = serializers.SerializerMethodField()
    class Meta:
        model = StudentProfile
        fields = (
            'get_lastname',
            'get_firstname',
            'get_birth_date',
            'bio'
        )
    def get_lastname(self, obj):
        return obj.lastname
    def get_firstname(self, obj):
        return obj.firstname
    def get_birth_date(self, obj):
        return obj.birth_date
    def get_bio(self, obj):
        return obj.bio