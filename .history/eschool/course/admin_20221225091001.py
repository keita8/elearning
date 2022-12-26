from django.contrib import admin
from .models import *

@admin.register()

admin.site.register(Course)
admin.site.register(Classe)
