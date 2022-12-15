from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)


class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    cvv = models.CharField(max_length=255)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
