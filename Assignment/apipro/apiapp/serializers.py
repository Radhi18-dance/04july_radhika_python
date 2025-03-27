from rest_framework import serializers
from .models import *

class stdSerial(serializers.ModelSerializer):
    class Meta:
        model=stdinfo
        fields='__all__'