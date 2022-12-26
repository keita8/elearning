from django.shortcuts import render
from django.http import *

def api_view(request, *args, **kwargs):
    data = {
        'nom': 'abdul'
    }