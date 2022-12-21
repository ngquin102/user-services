from rest_framework import serializers
<<<<<<< HEAD
from .models import User, PaymentMethod, Payments, Subscription
=======
from .models import User, PaymentMethod, Payments, Subscription,Product

>>>>>>> 5ea2c5064cbcf751c2b8b91f469fb851b8fd7b12

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

<<<<<<< HEAD

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'product', 'payment_method', 'start_date', 'end_date', 'active']
=======
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
>>>>>>> 5ea2c5064cbcf751c2b8b91f469fb851b8fd7b12
