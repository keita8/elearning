from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    get_user = serializers.SerializerMethodField(readonly=)
    class Meta:
        model = TeacherProfile
        fields = ('get_user', 'firstname', 'lastname', 'bio', 'phone_number')
    
    def dehydrate_get_user(self, obj):
        return obj.user
    
# class UserSerializer(serializers.ModelSerializer):
#     get_email = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = User
#         fields = ('get_email', 'is_staff', 'is_student', 'is_teacher', 'is_superuser', 'is_active', 'date_joined', 'last_login')
    
#     def get_email(self, obj):
#         return obj.email