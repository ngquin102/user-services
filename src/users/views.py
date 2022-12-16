from rest_framework.views import APIView 
from rest_framework.response import Response
from users.models import User, PaymentMethod, Payments, Subscription
from users.serializers import PaymentsSerializer, PaymentMethodSerializer, UserSerializer, SubscriptionSerializer
import datetime
import logging 

logger = logging.getLogger(__name__)

# Create your views here.
class PaymentsHistory(APIView):

    def get(self, request, format=None):
        payments = Payments.objects.all()
        serializer = PaymentsSerializer(payments, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SubscriptionStatus(APIView):
        def get(self, request, user_id, product_id, format=None):
            user = User.objects.get(id=user_id)
            subscription = Subscription.objects.filter(user=user, product=product_id, active=True).first()
            response_data = {}

            if subscription:

                response_data = {
                    "user": {
                        "username": user.username,
                        "email": user.email,
                        "phone_number": user.phone_number
                    },
                    "subscription": {
                        "product": subscription.product_id,
                        "payment_method": subscription.payment_method_id,
                        "start_date": subscription.start_date,
                        "end_date": subscription.end_date,
                        "active": subscription.active
                    }
                }
                response_data["subscription_status"] = True
                return Response(response_data, status=200)
            else:
                response_data["subscription_status"] = False
                return Response(response_data, status=200)