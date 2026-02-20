from rest_framework.views import APIView
from rest_framework import permissions

from api.services.login_service import LoginService

class LoginView(APIView):
     permission_classes = [permissions.AllowAny]

     def post(self,request):
          data = request.data
          return LoginService(data).login()