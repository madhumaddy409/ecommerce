from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view



from homepageslider.models import homepageslider


@api_view(['GET','POST'])
def homepage(request):
    if request.method == "GET":
        products = list(homepageslider.objects.values())

        return JsonResponse(products, safe=False)

    else:
        return HttpResponse("get method")