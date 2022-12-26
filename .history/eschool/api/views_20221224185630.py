import json
from django.shortcuts import render
from django.http import *
import json
from django.forms.s

def api_view(request, *args, **kwargs):
    data = json.loads(request.body)
    pre_data = json.dumps(data)
    data['headers']=dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    data['post-data'] = dict(request.POST)
    print(data)
    return JsonResponse(data)