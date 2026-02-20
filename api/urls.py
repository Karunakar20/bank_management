from django.urls import path

from api.views.bank_management_views import AccountView,PayLoanView,CreateUserView,TakeLoanView,ApplyInterestView
from api.views.login_view import LoginView

urlpatterns = [
    path('account/<str:customer_id>/', AccountView.as_view(), name='account-detail'),
    path('loan/pay/', PayLoanView.as_view(), name='pay-loan'),
    path('account/apply/interest/', ApplyInterestView.as_view()),
    path('user/create/', CreateUserView.as_view(), name='create-user'),
    path('take/loan/', TakeLoanView.as_view(), name='take-loan'),
    path('login/', LoginView.as_view(), name='knox_login'),
]
