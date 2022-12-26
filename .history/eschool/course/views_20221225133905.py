from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from account.models import *


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = S.objects.all()
