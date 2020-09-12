from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=32,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60,null=True, blank=True)
    description = models.CharField(max_length=250,null=True, blank=True)
    availability = models.CharField(max_length=35,null=True, blank=True)
    image = models.CharField(max_length=250,null=True, blank=True)
    ratings = models.DecimalField(decimal_places=5,max_digits=30,null=True, blank=True)
    price = models.BigIntegerField(null=True, blank=True)
    brand = models.CharField(max_length=35,null=True, blank=True)

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
