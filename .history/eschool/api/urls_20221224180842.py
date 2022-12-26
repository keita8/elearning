from urllib.parse import urlparse
from django.urls import path

from eschool.api.views import api_view 

app_name = 'api'

urlpatterns = [
    path('', api_view, name='view'
]


