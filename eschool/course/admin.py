from ast import Sub
from django.contrib import admin
from .models import *


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    readonly_fields = ('slug', )
    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'standard', 'slug')
    
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'standard', 'subject', 'name', 'slug', 'created_at')
    list_display_links = ('instructor', 'standard', 'subject', 'name')


