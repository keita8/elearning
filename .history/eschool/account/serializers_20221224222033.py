from dataclasses import fields
from rest_framework import serializers
from django.conf import settings 
from .models import *

User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    lastname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
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
    
class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ('phone_number',)
        
class UserTeacherUpdateSerializer(serializers.ModelSerializer):
    profile = TeacherProfileSerializer(source="teacherprofile", many=False)

    class Meta:
        model = Account
        fields = ('email', 'profile')

        # Custom .update() method for serializer to handle UserProfile data update
        def update(self, instance, validated_data):
            userprofile_serializer = self.fields['profile']
            userprofile_instance = instance.userprofile
            userprofile_data = validated_data.pop('teacherprofile', {})

            # to access the UserProfile fields in here
            # mobile = userprofile_data.get('mobile')

            # update the userprofile fields
            userprofile_serializer.update(userprofile_instance, userprofile_data)

            instance = super().update(instance, validated_data)
            return instance
    
class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherProfile
        fields = ("firstname", "lastname", "sex")
