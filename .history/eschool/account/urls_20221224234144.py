from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("all-users/", views.list_user, name="user"),
    path("all-student/", views.all_student, name="student"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.sign, name="register"),
    path("student/", views.student_homepage, name="student"),
    path("teacher/", views.teacher_homepage, name="teacher"),
    path("profile/", views.teacher_profile, name="profile"),
    path("learner-profile/", views.student_profile, name="profile-student"),
    path("change-password/", views.password_change, name="change"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
]
