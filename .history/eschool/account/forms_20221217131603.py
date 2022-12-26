from django import forms 
from .models import *

class UserRegistrationForm(forms.Form):
    """UserRegistrationForm definition."""
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

    # TODO: Define form fields here
