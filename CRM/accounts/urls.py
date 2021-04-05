from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('logout/',views.logoutuser,name='logout'),


    path('products/',views.products,name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),

    path('create_oder/<str:pk>/',views.create_order,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),

    path('user-page/',views.userpage,name='user-page'),
    path('settings/',views.usersettings,name='user-settings')
]
