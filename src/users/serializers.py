from rest_framework import serializers
from .models import User, PaymentMethod, Payments, Subscription,Product


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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=['name','price','description']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subscription
        fields=['user','product','payment_method','start_date','end_date','active']

class InforSerializer(serializers.Serializer):
    name=serializers.CharField(required=True)
    age=serializers.IntegerField()