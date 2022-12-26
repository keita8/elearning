from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("api/", include("api.urls"), name="api"),
    path("admin/", admin.site.urls),
    path("accounts/", include("account.urls")),
    path("cours/", include("course.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "E-learning"
admin.site.site_title = "Interface d'administration"
admin.site.index_title = "Bienvenue sur la plateforme E-learning"
