from rest_framework.response import Response
from django.db import transaction

from api.api_models.bank_management_models import CustomUser,BankAccount,Loan,Roles,Status

class TakeLoanService:
     
     def __init__(self,data):
          self.data = data
          
     def manage(self):
          try:
               with transaction.atomic():
                    customer_id = self.data.get('customer_id')
                    amount = float(self.data.get('amount'))
                    
                    custom_user = CustomUser.objects.filter(customer_id=customer_id).first()
                         
                    if not custom_user:
                         return Response({"error": "User not found"}, status=403)
                    
                    bank_account = BankAccount.objects.filter(user = custom_user).first()
                    if bank_account:
                         loan = Loan.objects.create(account = bank_account,total_amount = amount,status = Status.PENDING)
                         
                    return Response({
                    "loan_id": loan.id,
                    "pending_amount": loan.total_amount
               })
               
          except Exception as e:
               return Response({"error": str(e)}, status=400)
     