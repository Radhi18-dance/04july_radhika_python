from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def getdata(request):
    sdata = Post.objects.all()
    serial = postSerial(sdata, many=True)
    return Response(serial.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getstid(request, id):
    try:
        sdata = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial = postSerial(sdata)
    return Response(serial.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def insert(request):
    if request.method == 'POST':
        serial = postSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def update(request, id):
    try:
        r=Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = postSerial(r)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serial = postSerial(data=request.data, instance=r)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def deleteid(request, id):
    try:
        r = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serial = postSerial(r)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        r.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def commentdata(request,post_id):
    if request.method=='GET':
        comments = Comment.objects.filter(post_id=post_id)
        if comments.exists():
            serializer = CommentSerial(comments, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Comment not found.'}, status=status.HTTP_404_NOT_FOUND)
     
    if request.method=='POST':
        serializer = CommentSerial(data=request.data)
        if serializer.is_valid():
            serializer.save(post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


