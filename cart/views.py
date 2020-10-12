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
            # print(username)
            user_id = User.objects.get(username=username).id
            # print(user_id)
            # product_id = request.data.get('id')
            actionType = request.data.get('actionType')
            size = request.data.get('qty')
            products = request.data.get('products')

            for value in products:
                # print(value)


                if CartProd.objects.filter(user_id_id=user_id,product_id=value['id']).exists():
                    for value in products:
                        old_size = CartProd.objects.get(user_id_id=user_id, product_id=value['id']).size
                        # print(old_size)
                        if actionType == "add":
                            for value in products:
                                old_size = CartProd.objects.get(user_id_id=user_id,product_id=value['id']).size
                                # print(old_size)
                                new_size = old_size+value['qty']
                                CartProd.objects.filter(user_id_id=user_id,product_id=value['id']).update(size=new_size)
                            data = "update cart"
                            return JsonResponse(data, safe=False)

                        elif actionType == "subtract":
                            for value in products:
                                old_size = CartProd.objects.get(user_id_id=user_id,product_id=value['id']).size
                                print(old_size)

                                if old_size==1:
                                    CartProd.objects.filter(user_id_id=user_id, product_id=value['id']).delete()

                                else:
                                    new_size = old_size - value['qty']
                                    if new_size ==0:
                                        CartProd.objects.filter(user_id_id=user_id, product_id=value['id']).delete()
                                    else:
                                        CartProd.objects.filter(user_id_id=user_id, product_id=value['id']).update(size=new_size)

                            data = "subtract cart"
                            return JsonResponse(data, safe=False)


                        elif actionType == "delete":
                            for value in products:
                                CartProd.objects.get(user_id_id=user_id, product_id=value['id']).delete()
                            data = "cart deleted"
                            return JsonResponse(data, safe=False)

                        else:
                            data = "missing parameter from front end"
                            return JsonResponse(data, safe=False)

                else:
                    for value in products:
                        print(value)


                        product_name = Product.objects.get(id=value['id']).name
                        product_category = Product.objects.get(id=value['id']).category
                        product_description = Product.objects.get(id=value['id']).description
                        product_availability = Product.objects.get(id=value['id']).availability
                        product_image = Product.objects.get(id=value['id']).image
                        product_ratings = Product.objects.get(id=value['id']).ratings
                        product_price = Product.objects.get(id=value['id']).price
                        product_brand = Product.objects.get(id=value['id']).brand

                        reg =CartProd(product_id_id=value['id'],user_id_id = user_id, name=product_name, category= product_category,
                                      description=product_description, availability=product_availability, image=product_image,
                                      price=product_price, brand=product_brand,size=value['qty'])
                        reg.save()

                    data = "product added"
                    return JsonResponse(data, safe=False)
        else:
            data = "invalid token"
            return JsonResponse(data, safe=False)
    else:
        data = "get method"
        return JsonResponse(data, safe=False)