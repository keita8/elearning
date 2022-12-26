from .models import *
from rest_framework import serializers
# from account.serializers import InstructorSerializer


class CourseSerializer(serializers.ModelSerializer):
    # instructor = InstructorSerializer(read_only=True) 
    class Meta:
        model = Subject
        fields = "__all__"


# class InstructorSerializer(serializers.ModelSerializer):
#     course = CourseSerializer(many=True, read_only=True)

#     class Meta:
#         model = Teacher
#         fields = ("id", "email", "course", "password")
