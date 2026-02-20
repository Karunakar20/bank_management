import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_management.settings')
django.setup()

from api.services.create_user_service import CreateUserService

def UsersInitializer():
     
     data = {
          "email":"manager@bank.com",
          "mobile_number":"9958230258",
          "role":"manager",
          "password": "securepass"
     }
     
     CreateUserService(data).manage()
     print("Successfully Initialized")
     

if __name__ == '__main__':
    UsersInitializer()