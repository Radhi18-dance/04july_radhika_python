from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET']) 
def getall(request):
    stdata=stdinfo.objects.all()
    serial=stdSerial(stdata,many=True)
    return Response(serial.data)

@api_view(['GET'])
def getstid(request,id):
    try:
        stid=stdinfo.objects.get(id=id)
    except stdinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serail=stdSerial(stid)
    return Response(serail.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deletestid(request,id):
    try:
        stid=stdinfo.objects.get(id=id)
    except stdinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serail=stdSerial(stid)
        return Response(serail.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        stdinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

