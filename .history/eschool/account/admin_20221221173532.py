from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from django.utils.html import format_html

User = get_user_model()

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
class UserInstanceInline(admin.TabularInline):
    model = User


class UserAdmin(BaseUserAdmin):
    def thumbnail(self, object):
        return format_html('img src="{}" width="30" style="border-radius: ')
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = (
        "email",
        "role",
        "is_active",
        "is_staff",
        "last_login",
        "date_joined",
    )
    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )
    filter_vertical = ()
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
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
    list_display = ("user", "lastname", "firstname")
    list_display_links = ("user", "lastname", "firstname")


admin.site.register(User, UserAdmin)
admin.site.register(Student, UserAdmin)
admin.site.register(Teacher, UserAdmin)
