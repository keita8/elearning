from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'role', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'role', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'role', 'is_staff', 'last_login')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'role')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    
    
class StudentAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'role', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'role', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'role', 'is_staff', 'last_login')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'role')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


class TeacherAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'role', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'role', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'role', 'is_staff', 'last_login')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'role')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)