from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path: ("", views.InstructorListView.as_view(), name="instructor");
    path("list-all/", views.CourseListView.as_view(), name="list-all"),
]
