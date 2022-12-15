from django.contrib import admin
from users.models import User, PaymentMethod, Payments
# Register your models here.

admin.site.register(User)
admin.site.register(Payments)
admin.site.register(PaymentMethod)