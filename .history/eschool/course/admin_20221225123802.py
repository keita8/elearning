from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "instructor", "year")
    list_display_links = (
        "name",
        "instructor",
    )


admin.site.register(Classe)
admin.site.register()