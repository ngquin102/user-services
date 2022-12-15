from rest_framework.views import APIView 
from rest_framework.response import Response
from users.models import User, PaymentMethod, Payments
from users.serializers import PaymentsSerializer

# Create your views here.
class PaymentsHistory(APIView):
    def get(self, request, format=None):
        payments = Payments.objects.all()
        serializer = PaymentsSerializer(payments, many=True)
        return Response(serializer.data)
