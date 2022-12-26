from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Student, StudentProfile, Teacher, TeacherProfile


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
    else:
        return render(request, )
    template_name = "account/login.html"
    context = {}
    return render(request, template_name, context)


def sign(request):
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
