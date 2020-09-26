from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *
from . import views
# from users.views import loginView,logoutView
# from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('addproduct/', views.addproduct,name='addproduct'),
    path('products/', views.products, name='products'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('image_upload', hotel_image_view, name='image_upload'),
    path('success', success, name='success'),
    path('register/',views.register,name="register"),
    path('login/',views.login, name='login'),
    path('category/',views.category, name='category'),
    path('brand/',views.brand, name='brand'),
    path('userprofile/',views.userprofile, name='userprofile'),



]+ static(settings.STATIC_URL,
           document_root = settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)