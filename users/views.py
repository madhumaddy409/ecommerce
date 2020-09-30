import json
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.utils import json

from .models import Product, Student
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import *







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
        category = request.data.get('category')
        description = request.data.get('description')
        availability = request.data.get('availability')
        image = request.data.get('image')
        ratings = request.data.get('ratings')
        price = request.data.get('price')
        brand = request.data.get('brand')
        print(name)

        reg = Product(name= name,category = category,description = description,availability = availability,image = image,ratings = ratings,price = price,brand = brand)
        reg.save()
        return HttpResponse("product taken")
    else:
        return HttpResponse("get method")


@api_view(['GET','POST'])
def products(request):
    if request.method == "GET":
        products = list(Product.objects.values())

        return JsonResponse(products, safe=False)

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





@api_view(['GET','POST'])
def register(request):
    if request.method == "POST":
        username = request.data.get('username')
        # firstname = request.POST['fristname']
        # lastname = request.POST['lastname']
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            data2 = "Username already taken";
            return JsonResponse(data2, safe=False)

        else:
            username_count = User.objects.filter(email=email).count()
            if username_count > 0:
                print("email is exist")
                data3 = "email already taken";
                return JsonResponse(data3, safe=False)
            else:
                reg = User.objects.create_user(username=username, email=email, password=password, is_staff="True")
                reg.save()
                token, created = Token.objects.get_or_create(user=reg)

                data =" register successfully";
                return JsonResponse(data, safe=False)



    else:
        data1 = "please try again";
        return JsonResponse(data1, safe=False)







@api_view(['GET','POST'])
def login(request):
    if request.method == "POST":
        firstname = request.data.get('username')
        password = request.data.get('password')
        # firstname = "madhu"
        # password = "4pm15cs409"
        print(firstname)

        user = auth.authenticate(username=firstname, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['username'] = user.username
            user_name = request.session.get('username')
            # token = Token.objects.get(user=user).key
            # data['token'] = token
            # data ="login successfully";
            data = user_name
            return JsonResponse(data, safe=False)
        else:
            data = "login invalid"
            return JsonResponse(data, safe=False)

    else:
        data = "get method"
        return JsonResponse(data, safe=False)


@api_view(['GET', 'POST'])
def category(request):
    if request.method == "GET":
        category = list(Category.objects.values())

        return JsonResponse(category, safe=False)

    else:
        return HttpResponse("get method")

@api_view(['GET', 'POST'])
def brand(request):
    if request.method == "GET":
        brand = list(Brand.objects.values())

        return JsonResponse(brand, safe=False)

    else:
        return HttpResponse("get method")


@api_view(['GET', 'POST'])
def userprofile(request):
    if request.method == "POST":
        user_name = request.session.get('username')
        print(user_name)
        return JsonResponse(user_name, safe=False)
    #     if user_name is None:
    #         data = "please login";
    #         return JsonResponse(data, safe=False)
    #     else:
    #         # user = list(User.objects.values())
    #         user = list(User.objects.filter(username=user_name).values())
    #         return JsonResponse(user, safe=False)
    else:
        data1="get method"
        return JsonResponse(data1, safe=False)


