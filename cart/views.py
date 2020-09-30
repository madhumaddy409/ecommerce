from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view

from . models import CartProd


@api_view(['GET','POST'])
def cartProd(request):
    if request.method == "POST":
        token_data = request.headers.get('Authorization')
        if Token.objects.filter(key=token_data):
            username = Token.objects.get(key=token_data).user
            print(username)
            user_id = User.objects.get(username=username).id
            print(user_id )
            cart_prod = list(CartProd.objects.filter(user_id_id=user_id).values())
            return JsonResponse(cart_prod, safe=False)
        else:
            data = "invalid token"
            return JsonResponse(data, safe=False)

    else:
        data = "get method";
        return JsonResponse(data, safe=False)

@api_view(['GET','POST'])
def addcart(request):
    if request.method == "POST":
        product_id = request.data.get('product_id')
        user_id = request.data.get('user_id')
        name = request.data.get('name')
        category = request.data.get('category')
        description = request.data.get('description')
        availability = request.data.get('availability')
        image = request.data.get('image')
        price = request.data.get('price')
        brand = request.data.get('brand')
        size = request.data.get('size')
        # print(product_idd)

        reg =CartProd(product_id=product_id,user_id = user_id, name=name, category= category, description=description, availability=availability, image=image, price=price, brand=brand,size=size)
        reg.save()
        return HttpResponse("product added to cart")
    else:
        return HttpResponse("get method")