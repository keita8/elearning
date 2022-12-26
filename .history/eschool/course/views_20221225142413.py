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
    model = Standard
    template_name = 'courses/standard_list.html'
    context_object_name = 'standards'
    
    
class SubjectListView(DetailView):
    model = Standard
    template_name = 'courses/subject_list_view'


class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Subject.objects.all()
