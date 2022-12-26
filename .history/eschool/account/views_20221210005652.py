from django.shortcuts import render
from django.contrib.auth.decorators import (login_required, user_passes_test)
# Create your views here.
def login(request):
    template_name = "account/login.html"
    context = {}
    return render(request, template_name, context)


def sign(request):
    template_name = "account/sign.html"
    context = {}
    return render(request, template_name, context)
