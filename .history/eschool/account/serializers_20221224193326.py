from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('role', 'email', 'is_staff', 'is_student', 'is_teacher', 'is_superuser', 'is_active', 'date_joined', 'last_login')
        