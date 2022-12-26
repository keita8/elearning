from ast import Sub
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

# LISTE DE CLASSE
class StandardListView(ListView):
    model = Standard
    template_name = 'courses/standard_list.html'
    context_object_name = 'standards'
    

# LISTE DE COURS
class SubjectListView(DetailView):
    model = Standard
    template_name = 'courses/subject_list_view.html'
    context_object_name = 'standards'

    

# LISTE DES CHAPITRES DU COURS
class LessonListView(DetailView):
    model = Subject
    template_name = 'courses/lesson_list_view.html'
    context_object_name = 'subjects'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the books
    context['name'] = Standard.objects.all().first()
    return context



class CourseListView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Subject.objects.all()
