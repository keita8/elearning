
from django.contrib import admin
from django.urls import path, include 
from .views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='index')
]
