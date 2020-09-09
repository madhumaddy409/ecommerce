from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.utils import json

from .models import Product, Student
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *



# Create your views here.
def index(request):
    return render(request, 'users/index.html')

# @ensure_csrf_cookie
# @csrf_protect

@api_view(['GET','POST'])
def addstudent(request):
    if request.method == 'POST':
        firstname = request.data.get('firstname')
        email = request.data.get('email')
        reg = Student(firstname = firstname,email = email)
        reg.save()
        print(firstname);
        return HttpResponse('student added')
    else:
        return HttpResponse("get method")

@api_view(['GET','POST'])
def addproduct(request):
    if request.method == "POST":
        name = request.data.get('name')
        description = request.data.get('description')
        availability = request.data.get('availability')
        image = request.data.get('image')
        ratings = request.data.get('ratings')
        price = request.data.get('price')
        brand = request.data.get('brand')
        print(name)

        reg = Product(name= name,description = description,availability = availability,image = image,ratings = ratings,price = price,brand = brand)
        reg.save()
        return HttpResponse("product taken")
    else:
        return HttpResponse("get method")


@api_view(['GET','POST'])
def products(request):
    if request.method == "GET":
        products = Product.objects.all().values('id','name','description','price','image')

        return HttpResponse(products)
    else:
        return HttpResponse("get method")


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'users/imageupload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')