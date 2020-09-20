from django.http import HttpResponse
from django.shortcuts import render, redirect





# def cartProd(request):
from rest_framework.decorators import api_view

# from users.models import Product

from . models import CartProd


@api_view(['GET','POST'])
def cartProd(request):
    if request.method == "GET":
        CartProd = CartProd.objects.all().values('id','name','description','price','image')

        return HttpResponse(CartProd)
    else:
        return HttpResponse("get method")

@api_view(['GET','POST'])
def addcart(request):
    if request.method == "POST":
        product_id = request.data.get('product_id')
        name = request.data.get('name')
        description = request.data.get('description')
        availability = request.data.get('availability')
        image = request.data.get('image')
        price = request.data.get('price')
        brand = request.data.get('brand')
        size = request.data.get('size')
        print(name)

        reg = Product(name=name, description=description, availability=availability, image=image, price=price, brand=brand)
        reg.save()
        return HttpResponse("product added to cart")
    else:
        return HttpResponse("get method")