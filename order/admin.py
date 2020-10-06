from django.contrib import admin


# Register your models here.
from order.models import Order
from order.models import Payment


admin.site.register(Order)

admin.site.register(Payment)