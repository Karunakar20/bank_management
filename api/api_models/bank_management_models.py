from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Roles(models.TextChoices):
    CUSTOMER = 'customer', 'Customer'
    EMPLOYEE = 'employee', 'Employee'
    MANAGER = 'manager', 'Manager'
    
class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    COMPLETED = 'completed', 'Completed'

class CustomUserManager(BaseUserManager):

     def create_user(self, email, mobile_number, password=None, **extra_fields):
          if not email:
               raise ValueError("Email is required")

          if not mobile_number:
               raise ValueError("Mobile number is required")

          if not password:
               raise ValueError("Password is required")

          email = self.normalize_email(email)

          user = self.model(
               email=email,
               mobile_number=mobile_number,
               **extra_fields
          )

          user.set_password(password)
          user.save(using=self._db)
          return user


     # def create_superuser(self, email, mobile_number, password=None, **extra_fields):
     #      extra_fields.setdefault('is_staff', True)
     #      extra_fields.setdefault('is_superuser', True)

     #      if extra_fields.get('is_staff') is not True:
     #           raise ValueError("Superuser must have is_staff=True.")

     #      if extra_fields.get('is_superuser') is not True:
     #           raise ValueError("Superuser must have is_superuser=True.")

     #      return self.create_user(email, mobile_number, password, **extra_fields)

class CustomUser(AbstractBaseUser):

     email = models.EmailField(unique=True)
     mobile_number = models.CharField(max_length=15, unique=True)
     customer_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
     role = models.CharField(max_length=20,choices=Roles.choices)
     
     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = ['mobile_number']

     objects = CustomUserManager()
     
     class Meta:
          db_table='custom_user'

class BankAccount(models.Model):
     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='bank_account') # One to one field because a user cannot have multiple accounts
     balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
     
     class Meta:
          db_table='bank_account'
          
class Loan(models.Model):
     account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='loans')
     total_amount = models.DecimalField(max_digits=12, decimal_places=2)
     amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
     status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)

     class Meta:
          db_table='loans'

