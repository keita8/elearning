from django.shortcuts import render
from rest_framework import generics
from serializers import *
from 

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
