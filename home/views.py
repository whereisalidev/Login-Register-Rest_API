from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Registered Successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = User.objects.get(email=data['email'])
            if user.check_password(data['password']):
            # user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            # if user is not None:
                token, _ = Token.objects.get_or_create(user= user)
                return Response({'message': 'User Logged in Successfully', 'token': str(token)}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            