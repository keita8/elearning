from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from account.models import *
from 


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Subject.objects.all()
