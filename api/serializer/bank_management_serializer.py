from rest_framework import serializers
from api.api_models.bank_management_models import CustomUser,BankAccount,Loan,Roles

        
class BankAccountSerializer(serializers.ModelSerializer):
     class Meta:
        model = BankAccount
        fields = '__all__'
        
class LoanSerializer(serializers.ModelSerializer):
     class Meta:
        model = Loan
        fields = '__all__'
        
class CustomUserSerializer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = ['email', 'mobile_number', 'customer_id', 'role', 'is_active']
        


        

class AccountSerializer(serializers.ModelSerializer):

     class Meta:
          model = CustomUser
          fields = ['id']

     def to_representation(self, instance: CustomUser):
          ret = super().to_representation(instance)

          # 🔹 Customer (current instance)
          ret['customer'] = CustomUserSerializer(instance).data

          # 🔹 Bank Account
          bank_account = BankAccount.objects.filter(user=instance).first()

          ret['bank_account'] = (
               BankAccountSerializer(bank_account).data
               if bank_account else None
          )

          # 🔹 Loans
          loans = (
               Loan.objects.filter(account=bank_account)
               if bank_account else Loan.objects.none()
          )

          ret['loans'] = LoanSerializer(loans, many=True).data

          return ret
              
        
     
