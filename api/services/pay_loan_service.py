from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal

from api.api_models.bank_management_models import CustomUser,BankAccount,Loan,Roles,Status

class PayLoanService:
     def __init__(self,post_data):
          self.data = post_data['data']
          self.user = post_data['user']
          
     def manage(self):
          try:
               customer_id = self.data.get('customer_id')
               amount = float(self.data.get('amount'))
               
               if not customer_id or amount is None:
                    return Response({"error": "customer_id and amount are required."}, status=404)
               
               if amount <= 0:
                    return Response({"error": "Amount must be positive."}, status=400)
               
               custom_user = CustomUser.objects.filter(customer_id=customer_id).first()
                    
               if not custom_user:
                    return Response({"error": "User not found"}, status=403)
               
               # Permission Logic
               # Customer can only his/her own loan
               if self.user.role == Roles.CUSTOMER and self.user.customer_id != customer_id:
                    return Response({"error": "You can only pay for your own loans."}, status=403)
               
               # Employee or Manager: Can pay for any customer 
               if self.user.role in [Roles.EMPLOYEE] and self.user.role == Roles.EMPLOYEE:
                    return Response({"error": "Employees cannot manage other employees."}, status=403)

               # Checking user have account or not
               bank_account = BankAccount.objects.filter(user = custom_user).first()
               if not bank_account:
                    return Response({"error": "User has no bank account."}, status=400)
               
               # Get Active Loan
               loan = Loan.objects.filter(account=bank_account, status=Status.PENDING).first()
               if not loan:
                    return Response({"error": "No active loan found."}, status=400)
               
               # Validation for overpayment
               pending_amount = loan.total_amount - loan.amount_paid
               if amount > pending_amount:
                    return Response({"error": f"Amount exceeds pending loan amount ({pending_amount})."}, status=400)
               
               with transaction.atomic():
                    
                    amount = Decimal(str(amount)) 

                    loan.amount_paid += amount

                    if loan.amount_paid >= loan.total_amount:
                         loan.status = Status.COMPLETED

                    loan.save()

               return Response({
                    "loan_id": loan.id,
                    "pending_amount": loan.total_amount - loan.amount_paid,
                    "status":loan.status
               })
               
          except Exception as e:
               return Response({"error": str(e)}, status=400)

