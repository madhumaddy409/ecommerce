from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.orders, name='cart'),
    path('addorder/' ,views.addorder, name='addorder'),

]