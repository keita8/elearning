import json
from django.shortcuts import render
from django.http import *

def api_view(request, *args, **kwargs):
    data = {
        'name': 'abdul',
        'skill': 'python'
    }
    datas = json.loads(request.body)
    print(dta)
    return JsonResponse(data)