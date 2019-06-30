from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView
from apis.accounts.serializer import CreateUserSerializer

# Create your views here.

class CreateUserView(CreateAPIView):
    serializer=CreateUserSerializer()