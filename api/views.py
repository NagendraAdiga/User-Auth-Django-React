from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .serializers import UserSerializer

from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator


# Create your views here.


def home(request):
    return HttpResponse('Home Page')


@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request, user_obj)
            serializer = UserSerializer(user_obj)
            return Response("Login Successful", status=200)
        return Response('Username and password do not match!!')
