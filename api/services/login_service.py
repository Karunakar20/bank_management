from rest_framework.response import Response
from django.contrib.auth import authenticate
from knox.models import AuthToken

from api.serializer.bank_management_serializer import CustomUserSerializer

class LoginService():
     
     def __init__(self,data):
          self.data = data

     def login(self):
          email = self.data.get('email')
          password = self.data.get('password')
          
          if not email or not password:
               return Response({"error": "Please provide both email and password."}, status=400)
               
          user = authenticate(username=email, password=password)
          if user is not None:
               _, token = AuthToken.objects.create(user)
               return Response({
                    "user": CustomUserSerializer(user).data,
                    "token": token
               })
          else:
               return Response({"error": "Invalid credentials."}, status=401)