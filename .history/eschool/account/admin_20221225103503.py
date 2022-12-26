from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin


User = get_user_model()


class TeacherProfileResource(resources.ModelResource):
    birth_date = Field(column_name="Date de naissance")
    lastname = Field(column_name="Nom de famille")
    firstname = Field(column_name="Prénom")
    phone_number = Field(column_name="Téléphone")
    sex = Field(column_name="Genre")

    class Meta:
        model = TeacherProfile
        fields = (
            "sex",
            "user",
            "lastname",
            "firstname",
            "birth_date",
            "phone_number",
            "bio",
        )
        # export_order = ('user', 'lastname', 'firstname', 'phone_number', 'birth_date', 'bio', 'sex')

    def get_birth_date(self, obj):
        return obj.birth_date.strftime("%d/%m/%Y")

    def dehydrate_sex(self, obj):
        if obj.sex == "Monsieur":
            return obj.sex.HOMME
        return obj.sex.FEMME

    def dehydrate_phone_number(self, obj):
        return obj.phone_number

    def dehydrate_lastname(self, obj):
        return obj.lastname

    def dehydrate_firstname(self, obj):
        return obj.firstname

    def dehydrate_bio(self, obj):
        return obj.bio


@admin.register(TeacherProfile)
class TeacherAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = [TeacherProfileResource]
    list_display = ["user", "lastname", "firstname", "phone_number"]
    list_display_links = ["user", "lastname"]


# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)


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
    list_editable = ("is_active",)
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


# class TeacherProfileAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html(
#             f'img src="{object.image.url}" width="30" style="border-radius:50%";'
#         )

#     thumbnail.short_description = "Photo de profil"
#     list_display = ("user", "lastname", "firstname")
#     list_display_links = ("user", "lastname", "firstname")


admin.site.register(User, UserAdmin)
admin.site.register(Student, UserAdmin)
admin.site.register(Teacher, UserAdmin)
