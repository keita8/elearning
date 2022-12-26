from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from .models import Student, StudentProfile, Teacher, TeacherProfile
from django.template.loader import render_to_string
from .forms import *


# Create your views here.
# csrf_protect
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")  # Get password value from form
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_authenticated and user.role == "STUDENT":
                return redirect("accounts:student")
            elif user.is_authenticated and user.role == "TEACHER":
                return redirect("accounts:teacher")
            elif user.is_authenticated and user.role == "ADMIN":
                return HttpResponse("Page d'administrateur")
        else:
            return redirect("index")
    
    template_name = "account/login.html"
    context = {}
    return render(request, template_name, context)


def sign(request):
    form = UserRegistrationForm()
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(email=email, password=password)
            user.save()
            # ACTIVATION DU COMPTE
            current_site =get_current_site(request)
            email_subject = "Veuillez activer votre compte"
            message     =render_to_string(
                'account/account_activation_email.html',
                {
                    'user': user
                }
                )
            
            
    template_name = "account/sign.html"
    context = {}
    return render(request, template_name, context)


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
