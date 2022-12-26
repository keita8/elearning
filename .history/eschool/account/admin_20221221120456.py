from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import *

User = get_user_model()

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminCreationForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "role", "is_active", 'is_staff', 'last_login', 'date_joined']
    list_filter = ["role"]
    fieldsets = (
        (None, {"fields": ("email","role", "password")}),
        ("Informations personnelles", {"fields": ()}),
        ("Permissions", {"fields": ('is_active', "is_staff")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password", "password2")}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminCreationForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "role", "is_active", 'is_staff', 'last_login', 'date_joined']
    list_filter = ["role"]
    fieldsets = (
        (None, {"fields": ("email","role", "password")}),
        ("Informations personnelles", {"fields": ()}),
        ("Permissions", {"fields": ('is_active', "is_staff")}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password", "password2")}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


class StudentAdmin(BaseUserAdmin):
        # The forms to add and change user instances
    form = UserAdminCreationForm
    add_form = UserAdminCreationForm

    fieldsets = (
        (None, {"fields": ("email","password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password", "password2")}),
    )

    list_display = ("email", "role", "is_active", "last_login", "date_joined")
    list_filter = ("role", "is_active")
    search_fields = ("email", "role")
    ordering = ("email",)
    list_editable = ('is_active', )
    filter_horizontal = ()


class TeacherAdmin(BaseUserAdmin):
        # The forms to add and change user instances
    form = UserAdminCreationForm
    add_form = UserAdminCreationForm

    fieldsets = (
        (None, {"fields": ("email", "password", "last_login")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password", "password2")}),
    )

    list_display = ("email", "role", "is_active", "last_login", "date_joined")
    list_filter = ("role", "is_active")
    search_fields = ("email", "role")
    ordering = ("email",)
    list_editable = ('is_active', )
    filter_horizontal = ()


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
