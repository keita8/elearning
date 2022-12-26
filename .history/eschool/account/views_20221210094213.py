from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import (login_required, user_passes_test)

from .models import Student, Teacher
# Create your views here.
# csrf_protect
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email') 
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(user.role)
            # is_student = Teacher.objects.get(email=user)
            # if user.is_authenticated and is_student:
            #     return HttpResponse('page étudiant') 
            # elif user.is_authenticated and type_obj.is_teach:
            #     return redirect('thome') 
        else:
            return redirect('index')
        
    template_name = 'account/login.html'
    context = {}
    return render(request, template_name, context)


def sign(request):
    template_name = "account/sign.html"
    context = {}
    return render(request, template_name, context)
