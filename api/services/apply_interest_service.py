from rest_framework.response import Response

from api.tasks import apply_interest_task

class ApplyInterestService:
     def __init__(self,data):
          self.data = data
          
     def manage(self):
          
          interest_percent = self.data.get('interest_percent')
          if interest_percent is None:
               return Response({"error": "interest_percent is required."}, status=400)
          
          try:
               interest_percent = float(interest_percent)
               if interest_percent < 0:
                    return Response({"error": "Interest percent cannot be negative."}, status=400)
          except ValueError:
               return Response({"error": "Invalid interest_percent."}, status=400)

          apply_interest_task.delay(interest_percent)
          
          return Response({"message": "Interest application started. Check task status for results."})