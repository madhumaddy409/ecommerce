from django.http import HttpResponse
from django.shortcuts import render, redirect


from rest_framework.decorators import api_view

from . models import CartProd


@api_view(['GET','POST'])
def cartProd(request):
    if request.method == "GET":
        CartProducts = CartProd.objects.all().values('product_id','id','name','description','price','image')

        return HttpResponse(CartProducts)
    else:
        return HttpResponse("get method")

@api_view(['GET','POST'])
def addcart(request):
    if request.method == "POST":
        product_id = request.data.get('product_id')
        name = request.data.get('name')
        category = request.data.get('category')
        description = request.data.get('description')
        availability = request.data.get('availability')
        image = request.data.get('image')
        price = request.data.get('price')
        brand = request.data.get('brand')
        size = request.data.get('size')
        # print(product_idd)

        reg = Product(product_id=product_id, name=name, category= category, description=description, availability=availability, image=image, price=price, brand=brand)
        reg.save()
        return HttpResponse("product added to cart")
    else:
        return HttpResponse("get method")