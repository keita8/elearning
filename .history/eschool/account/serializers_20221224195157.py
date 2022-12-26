from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    get_user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = StudentProfile
        fields = (
            "user",
            "sex",
            "lastname",
            "firstname",
            "birth_date",
            "phone_number",
            "bio",
            "avatar",
        )
    
# class UserSerializer(serializers.ModelSerializer):
#     get_email = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = User
#         fields = ('get_email', 'is_staff', 'is_student', 'is_teacher', 'is_superuser', 'is_active', 'date_joined', 'last_login')
    
#     def get_email(self, obj):
#         return obj.email