from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = "account"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("sign-in/", views.sign, name="sign"),
]
