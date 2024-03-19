from django.shortcuts import render

# Create your views here.
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def register(request):
    #ID ,PW -> 요청
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    
@api_view(["GET"])
def me(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=200)