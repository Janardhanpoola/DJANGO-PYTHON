"""DRF4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from testapp import views

from rest_framework import routers

router=routers.DefaultRouter()

router.register('api',views.EmployeeCRUDCBV)

from rest_framework.authtoken import views  #this is the library for auth token

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token #3rd party jwt token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #path('get-api-token',views.obtain_auth_token,name='get-api-token')  #you need to call the class obtain_auth_token for generating token for a particualr user

    #from cmd type --->http http://127.0.0.1:8000/get-api-token username="jpoola" password="123"  ...you'll get the token for that user

    #if token is already generated from django-admin it will show that token...else it will generate a new token


    path('auth-jwt/',obtain_jwt_token), #from cmd if you need to obtain token ...http://127.0.0.1:8000/auth-jwt/  username="jpoola"   password="123"
                                        # from postman issue http://127.0.0.1:8000/auth-jwt/ ..provide username and pwd in Body section and "POST" request  and not "GET"                           


    path('auth-jwt-refresh/',refresh_jwt_token), #to perform refresh token...we need to specify lines 60 to 63 in settings.py

                                                # from cmd http http://127.0.0.1:8000/auth-jwt-refresh/ token=<<exisiting token>> it provides a new token

                                                # from postman issue http://127.0.0.1:8000/auth-jwt-refresh/ ...specify Content-Type application/json in header section and token <<token>> in body section 

    path('auth-jwt-verify/',verify_jwt_token) # from cmd issue http http://127.0.0.1:8000/auth-jwt-verify/ token=<<token>>..returns same token if exists else throws token expire msg
                                              # from postman specify Content-Type application/json in header section and token <<token>> in body section                        

    # token is in the form xxx.yy.zzz where x is header,y is payload,z is signature
]
