from django.shortcuts import render
from rest_framework import generics

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = 
