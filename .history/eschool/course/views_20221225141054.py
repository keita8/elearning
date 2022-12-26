from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from account.models import *
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    FormView
)


class StandardListView(ListView):
    conte


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Subject.objects.all()
