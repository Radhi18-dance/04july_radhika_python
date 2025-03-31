from rest_framework import serializers
from .models import *

class postSerial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerial(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 