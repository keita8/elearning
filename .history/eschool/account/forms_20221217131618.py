from pyexpat import model
from django import forms 
from .models import *

class UserRegistrationForm(forms.Form):
    """UserRegistrationForm definition."""
    class Meta:
        model = User

    # TODO: Define form fields here
