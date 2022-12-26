from dataclasses import field, fields
from pyexpat import model
from django import forms 
from django.conf import settings 
from .models import *

User = settings.AUTH_USER_MODEL

class UserRegistrationForm(forms.Form):
    """UserRegistrationForm definition."""
    class Meta:
        model = User
        fields = ('email',)

    # TODO: Define form fields here
