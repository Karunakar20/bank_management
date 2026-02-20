from celery import shared_task
from decimal import Decimal
from django.db import transaction

from api.api_models.bank_management_models import BankAccount,Roles

@shared_task
def apply_interest_task(interest_percent):

     updated_list = []

     try:
          # Convert to Decimal (IMPORTANT)
          interest_percent = Decimal(str(interest_percent))

          accounts = BankAccount.objects.filter(
               user__role=Roles.CUSTOMER
          )

          for account in accounts:

               old_balance = account.balance  # already Decimal

               interest_amount = (old_balance * interest_percent) / Decimal("100")
               new_balance = old_balance + interest_amount

               with transaction.atomic():
                    account.balance = new_balance
                    account.save(update_fields=["balance"])

               updated_list.append({
                    "customer_id": account.user.customer_id,
                    "old_balance": float(old_balance),
                    "new_balance": float(new_balance)
               })

          return {
               "updated_count": len(updated_list),
               "updated_accounts": updated_list
          }

     except Exception as e:
          return f"Error applying interest: {str(e)}"

     