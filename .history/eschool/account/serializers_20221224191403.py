from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('role', 'email', 'is_staff', 'is_student', 'is_teacher', '')