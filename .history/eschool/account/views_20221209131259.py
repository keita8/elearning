from django.shortcuts import render

# Create your views here.
def login(request):
    template_name = 'account/login.html'
    context = {}
    return render(request, template_name, context)

def sign(request):
    template_name = 'account/sign.html'
    context = {}
    return render(request, template_name, context)