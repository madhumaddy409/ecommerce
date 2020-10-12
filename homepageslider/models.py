from django.db import models
from users.models import Product
# Create your models here.
class homepageslider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default="")
    status = models.CharField(max_length=60, null=True, blank=True)

