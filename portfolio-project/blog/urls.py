
from django.urls import path
from . import views

from django.urls import include


urlpatterns = [
    path('', views.allblogs,name="allblogs"),
    path('<int:blog_id>/',views.detail,name='detail'),  #url path if user specifies integer after blog..for ex..blog/1 or blog/2
] 