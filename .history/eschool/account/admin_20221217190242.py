from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "role", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "role", "password1", "password2"),
            },
        ),
    )

    list_display = ("email", "role", "is_admin", "last_login")
    list_filter = ("role", "is_admin", "is_active", "  ")
    search_fields = ("email", "role")
    ordering = ("email",)
    filter_horizontal = (
        "  ",
        "user_permissions",
    )


class StudentAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "role", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_display = ("email", "role", "last_login")
    list_filter = ("role", "is_admin", "is_active", "  ")
    search_fields = ("email", "role")
    ordering = ("email",)
    filter_horizontal = (

        "user_permissions",
    )


class TeacherAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "role", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_display = ("email", "role","last_login")
    list_filter = ("role", "is_admin", "is_active", "  ")
    search_fields = ("email", "role")
    ordering = ("email",)
    filter_horizontal = (
        "  ",
        "user_permissions",
    )


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "lastname", "firstname")
    list_display_links = ("user", "lastname", "firstname")


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "lastname", "firstname")
    list_display_links = ("user", "lastname", "firstname")


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
