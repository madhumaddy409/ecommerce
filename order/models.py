from django.db import models
from users.models import Product
from django.contrib.auth.models import User


# Create your models here.


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    price = models.BigIntegerField(null=True, blank=True)
    quantity = models.BigIntegerField(null=True,blank=True)
    address = models.CharField(max_length=800, null=True, blank=True)
    orderdate = models.DateTimeField(auto_now_add=True, blank=True)
    ordersatus = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    payment_method = models.CharField(max_length=25, null=True, blank=True)

