import json
from django.shortcuts import render
from django.http import *
import json
from django.forms.models import model_to_dict
from rest_framework.response import *
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def api_view(request, *args, **kwargs):
    
    if
    data = json.loads(request.body)
    pre_data = json.dumps(data)
    data['headers']=dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)
    data['post-data'] = dict(request.POST)
    print(data)
    return Response(data)