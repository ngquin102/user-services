from rest_framework import serializers
from .models import User, PaymentMethod, Payments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['id', 'user', 'payment_method', 'amount', 'date']


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'user', 'name', 'card_number', 'cvv', 'expiry_date']
