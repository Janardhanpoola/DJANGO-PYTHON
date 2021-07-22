"""DRF2 URL Configuration

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
from django.urls import path,re_path


from testapp  import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('api/',views.EmployeeListAPIView.as_view()),

    path('api/',views.EmployeeListCreateAPIView.as_view()),
    
    #re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeRetrieveAPIView.as_view())  # P refers to named group expression ...In Python regular expressions, the syntax for named regular expression groups is (?P<name>pattern), where name is the name of the group and pattern is some pattern to match.


    #re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeUpdateAPIView.as_view())

   #re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeDestroyAPIView.as_view())
    #re_path(r'api/<int:id>',views.EmployeeRetrieveAPIView.as_view())

   # re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeRetrieveUpdateAPIView.as_view())

    #re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeRetrieveDestroyAPIView.as_view())

    re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeRetrieveUpdateDestroyAPIView.as_view())

    #re_path(r'^api/(?P<pk>\d+)/$',views.EmployeeListCreateAPIViewM.as_view())


    #path('api/',views.EmployeeCreateAPIView.as_view())
]
