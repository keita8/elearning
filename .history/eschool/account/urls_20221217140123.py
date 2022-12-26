from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("sign-in/", views.sign, name="sign"),
    path("student/", views.student_homepage, name="student"),
    path("teacher/", views.teacher_homepage, name="teacher"),
    path('activate/<>/<>', views.activate, name='activate'),
]
