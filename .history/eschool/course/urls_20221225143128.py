from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path("list-all/", views.CourseListView.as_view(), name="list-all"),
    path('niveau/', views.StandardListView.as_view(), name='standard'),
    path('<slug>/', views.)
]
