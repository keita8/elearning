from ast import Sub
from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "instructor", "year")
    list_display_links = (
        "name",
        "instructor",
    )


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
    li


admin.site.register(Classe)

admin.site.register(Lesson)