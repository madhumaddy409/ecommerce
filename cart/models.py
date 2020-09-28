
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Product


class CartProd(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,default="")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=60, null=True, blank=True)
    category = models.CharField(max_length=60, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    availability = models.CharField(max_length=35, null=True, blank=True)
    image = models.CharField(max_length=250, null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    brand = models.CharField(max_length=35, null=True, blank=True)
    size = models.BigIntegerField(null=True,blank=True)