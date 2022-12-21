from rest_framework.views import APIView 
from rest_framework.response import Response
from users.models import User, PaymentMethod, Payments, Product, Subscription
from users.serializers import PaymentsSerializer, PaymentMethodSerializer, UserSerializer, SubscriptionSerializer, ProductSerializer
from .serializers import InforSerializer
from rest_framework import status
# Create your views here.
class PaymentsHistory(APIView):
    
    def get(self, request, format=None):
        payments = Payments.objects.all()
        serializer = PaymentsSerializer(payments, many=True)
        return Response(serializer.data)


class SubscriptionAPIView(APIView):
    def get(self, request, format=None):
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data)
class TestAPIView(APIView):
    def get(self, request):
        return Response('oke')
    def post(selfself,request):
        da=InforSerializer(data=request.data)
        if not da.is_valid():
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)
        print(da.data)
        return Response(' nhan data thanh cong', status=status.HTTP_200_OK)