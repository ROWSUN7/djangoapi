from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from apis.accounts.serializer import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class CreateUserView(CreateAPIView):
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class UpdateUserView(UpdateAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]