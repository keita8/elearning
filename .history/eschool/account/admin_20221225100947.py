from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin


class TeacherResource(resources.ModelResource):
    lastname = Field(attribute='Nom de famille')
    
    class Meta:
        model = TeacherProfile
        # widgets = {
        # 'year': {'format': '%d.%m.%Y'},
        # }

class TeacherAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]
User = get_user_model()

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
class UserInstanceInline(admin.TabularInline):
    model = User


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = (
        "email",
        "role",
        "is_active",
        "is_admin",
        "is_staff",
        "last_login",
        "date_joined",
    )
    list_filter = ("role", "is_staff", "is_admin", "is_active")
    list_editable = ('is_active', )
    filter_vertical = ()
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "lastname", "firstname")
    list_display_links = ("user", "lastname", "firstname")


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            f'img src="{object.image.url}" width="30" style="border-radius:50%";'
        )

    thumbnail.short_description = "Photo de profil"
    list_display = ("user", "lastname", "firstname")
    list_display_links = ("user", "lastname", "firstname")


admin.site.register(User, UserAdmin)
admin.site.register(Student, UserAdmin)
admin.site.register(Teacher, UserAdmin)
