from .models import *
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class InstructorSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)
    id = 
    
    class Meta:
        model = Teacher
        fields = ('id', 'email', 'course', 'password')
