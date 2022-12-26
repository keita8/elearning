from django.contrib import admin
from .models import *

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'year')

admin.site.register(Course)
admin.site.register(Classe)
