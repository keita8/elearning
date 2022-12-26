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
    


admin.site.register(Classe)

admin.site.register(Subject)
admin.site.register(Lesson)