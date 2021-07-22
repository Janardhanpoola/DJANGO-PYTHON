
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('destination',views.dest,name='destination')
]
