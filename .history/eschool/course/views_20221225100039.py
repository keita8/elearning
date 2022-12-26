from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from account.models import *

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Teacher.teacher.all()


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Teacher.teacher.all()
