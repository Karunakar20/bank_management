from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.permissions.user_permissions import IsManager
from api.services.account_service import AccountService
from api.services.apply_interest_service import ApplyInterestService
from api.services.create_user_service import CreateUserService
from api.services.pay_loan_service import PayLoanService
from api.services.take_loan_service import TakeLoanService

class AccountView(APIView):
     def get(self,request,customer_id):
          user = request.user  
          return AccountService(user).get(customer_id)
     
class ApplyInterestView(APIView):
     permission_classes = [IsAuthenticated, IsManager]
     
     def post(self,request):
          data = request.data
          return ApplyInterestService(data).manage()
     
class CreateUserView(APIView):
     
     permission_classes = [IsAuthenticated, IsManager]
     
     def post(self,request):
          data = request.data
          return CreateUserService(data).manage()
     
class PayLoanView(APIView):
     def post(self,request):
          data = request.data
          user = request.user
          
          post_data = {
               'data': data,
               'user': user
          }
          
          return PayLoanService(post_data).manage()
     
class TakeLoanView(APIView):
     def post(self,request):
          
          data = request.data
          return TakeLoanService(data).manage()
     
     