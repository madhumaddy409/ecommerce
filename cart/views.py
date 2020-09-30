from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view

from . models import CartProd
from users.models import Product

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
        token_data = request.headers.get('Authorization')
        if Token.objects.filter(key=token_data):
            username = Token.objects.get(key=token_data).user
            print(username)
            user_id = User.objects.get(username=username).id
            print(user_id)
            product_id = request.data.get('id')
            size = request.data.get('qty')

            product_name = Product.objects.get(id=product_id).name
            product_category = Product.objects.get(id=product_id).category
            product_description = Product.objects.get(id=product_id).description
            product_availability = Product.objects.get(id=product_id).availability
            product_image = Product.objects.get(id=product_id).image
            product_ratings = Product.objects.get(id=product_id).ratings
            product_price = Product.objects.get(id=product_id).price
            product_brand = Product.objects.get(id=product_id).brand

            print(product_id)
            reg =CartProd(product_id_id=product_id,user_id_id = user_id, name=product_name, category= product_category,
                          description=product_description, availability=product_availability, image=product_image,
                          price=product_price, brand=product_brand,size=size)
            reg.save()

            data = "product added"
            return JsonResponse(data, safe=False)
        else:
            data = "invalid token"
            return JsonResponse(data, safe=False)
    else:
        data = "get method"
        return JsonResponse(data, safe=False)