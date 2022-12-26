import json
from django.shortcuts import render
from django.http import *
import json

def api_view(request, *args, **kwargs):
    data = {
        'name': 'abdul',
        'skill': 'python'
    }
    data = json.loads(request.body)
    data['headers']=dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)