from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from users.models import Product
from django.http import HttpResponse, JsonResponse

from . models import Order


@api_view(['GET','POST'])
def orders(request):
    if request.method == "POST":
        token_data = request.headers.get('Authorization')
        if Token.objects.filter(key=token_data):
            username = Token.objects.get(key=token_data).user
            print(username)
            user_id = User.objects.get(username=username).id
            print(user_id )
            orders = list(Order.objects.filter(user_id=user_id).values())
            return JsonResponse(orders, safe=False)
        else:
            data = "invalid token"
            return JsonResponse(data, safe=False)

    else:
        data = "get method";
        return JsonResponse(data, safe=False)


@api_view(['GET','POST'])
def addorder(request):
    if request.method == "POST":
        token_data = request.headers.get('Authorization')
        if Token.objects.filter(key=token_data):
            username = Token.objects.get(key=token_data).user
            print(username)
            user_id = User.objects.get(username=username).id
            print(user_id)
            product_id = request.data.get('id')
            quantity = request.data.get('qty')
            address = request.data.get('address')
            Ordersatus = "Pending"

            product_price = request.data.get('price')


            print(product_id)
            reg = Order(product_id=product_id,user_id=user_id,price=product_price,quantity=quantity,address=address,ordersatus=Ordersatus)
            reg.save()

            data = "order placed"
            return JsonResponse(data, safe=False)
        else:
            data = "invalid token"
            return JsonResponse(data, safe=False)
    else:
        data = "get method"
        return JsonResponse(data, safe=False)