from rest_framework.response import Response

from api.api_models.bank_management_models import CustomUser,Roles,BankAccount,Loan
from api.serializer.bank_management_serializer import AccountSerializer,CustomUserSerializer,LoanSerializer,BankAccountSerializer

class AccountService:
     
     def __init__(self,user):
          self.user = user
          
     def __validations(self):
          

          # CUSTOMER trying to access another customer
          if self.user.role == Roles.CUSTOMER:
               if self.user.customer_id != self.id:
                    return False

          # EMPLOYEE trying to access another employee
          elif self.user.role == Roles.EMPLOYEE:
               target_user = CustomUser.objects.filter(customer_id=self.id).first()
               if target_user and target_user.customer_id != self.id:
                    return False

          # If no restriction triggered → allow
          return True
     
     def get(self,customer_id):
          try:
               self.id = customer_id
               val = self.__validations()
               
               if not val:
                    return Response({"error": "Access denied"}, status=403)
               
               custom_user = CustomUser.objects.filter(customer_id=self.id).first()
               
               if not custom_user:
                    return Response({"error": "User not found"}, status=403)
               
               if custom_user.role == Roles.EMPLOYEE:
                    user = CustomUser.objects.filter(role = Roles.CUSTOMER)
                    
               if custom_user.role == Roles.CUSTOMER:
                    user = CustomUser.objects.filter(customer_id = self.id, role= Roles.CUSTOMER)
                    
               if custom_user.role == Roles.MANAGER:
                    user = CustomUser.objects.filter(role__in= [Roles.CUSTOMER,Roles.EMPLOYEE])
 
               response = AccountSerializer(user,many=True).data

               return Response(response, status=403)
          
          except Exception as e:
               return Response({"error": str(e)}, status=400)
          
          
               
          
          
          
                         

               
          
