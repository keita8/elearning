from operator import methodcaller
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    methodcaller