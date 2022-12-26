from dataclasses import field, fields
from pyexpat import model
from django import forms 
from django.conf import settings 
from .models import *

User = settings.AUTH_USER_MODEL

class UserRegistrationForm(forms.Form):
    """UserRegistrationForm definition."""
    email = forms.EmailField(w)
    class Meta:
        model = User
        fields = ('email', 'password')

    # TODO: Define form fields here
