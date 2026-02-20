from rest_framework.response import Response
from django.db import transaction

from api.api_models.bank_management_models import CustomUser,Roles,BankAccount
from api.serializer.bank_management_serializer import CustomUserSerializer
import uuid

class CreateUserService:
     def __init__(self,data):
          self.data = data
          
     def __reqData(self):
          self.password = self.data.get('password',None)
          self.email = self.data.get('email',None)
          self.mobile_number = self.data.get('mobile_number',None)
          self.role = self.data.get('role',None)
          
     def __validate(self):
          if not self.email:
               return Response({"error": "Email is required."}, status=400)

          if not self.mobile_number:
               return Response({"error": "Mobile number is required."}, status=400)

          if not self.password:
               return Response({"error": "Password is required."}, status=400)

          if not self.role:
               return Response({"error": "Role is required."}, status=400)

          if self.role not in Roles.values:
               return Response({"error": "Invalid role."}, status=400)
               
          
     def manage(self):
          self.__reqData()
          validation_error = self.__validate()

          if validation_error:
               return validation_error

          try:
               with transaction.atomic():

                    user = CustomUser.objects.create_user(
                         email=self.email,
                         mobile_number=self.mobile_number,
                         password=self.password,
                         role=self.role
                    )
                    
                    if user.role == Roles.EMPLOYEE:
                         user.customer_id = f"EMPL{str(uuid.uuid4().int)[:6]}"
                         user.save()
                         
                    if user.role == Roles.MANAGER:
                         user.customer_id = f"MANR{str(uuid.uuid4().int)[:6]}"
                         user.save()
                         
                    # If role is CUSTOMER  create customer_id and bank account
                    if user.role == Roles.CUSTOMER:
                         user.customer_id = f"CUST{str(uuid.uuid4().int)[:6]}"
                         user.save()

                         BankAccount.objects.create(user=user,balance=10000)

                    return Response(f"{user.role} create successfully",status=201)

          except Exception as e:
               return Response({"error": str(e)}, status=400)