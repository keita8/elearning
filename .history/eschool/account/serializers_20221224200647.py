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
    get_email = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = (
            'email',
        )
    
    def get_email(self, obj):
        return obj.email