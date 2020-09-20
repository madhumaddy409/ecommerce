from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.cartProd, name='cart'),
    path('addcart/' , views.addcart, name='addcart'),
]