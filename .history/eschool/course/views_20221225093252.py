from django.shortcuts import render
from rest_framework import generics
from serializers import *

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
