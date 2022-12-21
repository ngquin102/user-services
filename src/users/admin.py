from django.contrib import admin
from users.models import User, PaymentMethod, Payments,Subscription,Product
# Register your models here.

admin.site.register(User)
admin.site.register(Payments)
admin.site.register(PaymentMethod)
admin.site.register(Product)
admin.site.register(Subscription)