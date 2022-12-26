from base64 import urlsafe_b64encode
from email.message import *
from django.core.mail import *
from django.contrib.auth.tokens import *
from django.utils.http import (
    url_has_allowed_host_and_scheme,
    urlsafe_base64_decode,
    urlsafe_base64_encode,
)
from django.utils.http import *
from django.utils import *
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from .models import *
from django.template.loader import render_to_string
from .forms import *
import codecs
import datetime
import locale
from decimal import Decimal
from urllib.parse import quote
from django.utils.functional import Promise
from django.utils.encoding import force_bytes




# Create your views here.
# csrf_protect
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")  # Get password value from form
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_authenticated and user.role == "STUDENT":
                return redirect("accounts:student")
            elif user.is_authenticated and user.role == "TEACHER":
                return redirect("accounts:teacher")
            elif user.is_authenticated and user.role == "ADMIN":
                return HttpResponse("Page d'administrateur")
            
    template_name = "account/login.html"
    context = {}
    return render(request, template_name, context)



@login_required(login_url='accounts:login')
def teacher_profile(request):
    if request.method == 'POST':
        user = UserLoginForm(request.POST, instance=request.user)
        profile = TeacherProfileForm(request.POST, request.FILES, instance=user.user)
        if user_form.is_valid() and profile_form.is_valid():
            
    return


def sign(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(email=email, password=password)
            user.save()
            return HttpResponse(user)
            # ACTIVATION DU COMPTE
            current_site = get_current_site(request)
            email_subject = "Veuillez activer votre compte"
            message = render_to_string(
                "account/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            to_email = email
            send_mail = EmailMessage()
    else:
        form = UserRegistrationForm()

    template_name = "account/sign.html"
    context = {
        "form": form,
    }
    return render(request, template_name, context)


@login_required(login_url="accounts:login")
def logout_user(request):
    user = request.user
    logout(request)
    return redirect("index")


def student_homepage(request):
    if request.user.is_authenticated and request.user.role == "STUDENT":
        user = StudentProfile.objects.get(user=request.user)
        context = {"user": user}
        return render(request, "layouts/student_homepage.html", context)
    else:
        return redirect("accounts:login")


def teacher_homepage(request):
    if request.user.is_authenticated and request.user.role == "TEACHER":
        user = TeacherProfile.objects.get(user=request.user)
        context = {"user": user}
        return render(request, "layouts/teacher_homepage.html", context)
    else:
        return redirect("accounts:login")


# ACTIVATION DU COMPTE
def activate(request, uidb64, token):
    pass
