from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import (login_required, user_passes_test)
# Create your views here.
def login_user(request):
    
    if request.method == 'POST':
        email = request.POST.get('email') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponse(user)
            # type_obj = user_type.objects.get(user=user)
            # if user.is_authenticated and type_obj.is_student:
            #     return redirect('shome') #Go to student home
            # elif user.is_authenticated and type_obj.is_teach:
            #     return redirect('thome') #Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('index')
    template_name = 'layouts/index.html'
    context = {}
    return render(request, template_name, context)


def sign(request):
    template_name = "account/sign.html"
    context = {}
    return render(request, template_name, context)
