from operator import itemgetter

from django.shortcuts import render

# Create your views here.
from psycopg2._psycopg import cursor
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import json
from users.models import Product
from django.http import HttpResponse, JsonResponse


from . models import CartProd
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
        product = json.loads(request.body)


        token_data = request.headers.get('Authorization')
        if Token.objects.filter(key=token_data):
            username = Token.objects.get(key=token_data).user
            user_id = User.objects.get(username=username).id

            phone_number = product['phone']
            address = product['address']
            Ordersatus = "pending"
            payment_method = product['payment_method']

            products = request.data.get('products')
            for value in products:
                print(value)



                reg = Order(product_id=value['id'], user_id=user_id, price=0, quantity=value['qty'],
                            address=address, ordersatus=Ordersatus, phone_number=phone_number,
                            payment_method=payment_method)
                reg.save()
                CartProd.objects.get(user_id_id=user_id, product_id=value['id']).delete()

            # product_id = request.pro['payment_method']
            # print(product_id)

            data ="order placed"
            return JsonResponse(data, safe=False)
        else:
            data = "invalid token"
            return JsonResponse(data, safe=False)
    else:
        data = "get method"
        return JsonResponse(data, safe=False)