from rest_framework import serializers
from .models import User, PaymentMethod, Payments, Subscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['id', 'user', 'payment_method', 'amount', 'date']


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'user', 'name', 'card_number', 'cvv', 'expiry_date']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'product', 'payment_method', 'start_date', 'end_date', 'active']
