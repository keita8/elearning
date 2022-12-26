import json
from django.shortcuts import render
from django.http import *

def api_view(request, *args, **kwargs):
    data = {
        'name': 'abdul',
        'skill': 'python'
    }
    data = json.loads(request.body)
    data['content_type'] = req
    print(data)
    return JsonResponse(data)