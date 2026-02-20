from rest_framework.permissions import BasePermission
from api.api_models.bank_management_models import Roles

class IsManager(BasePermission):
     message = "Only Managers are allowed."

     def has_permission(self, request, view):
          return (
               request.user.is_authenticated and
               request.user.role == Roles.MANAGER
          )