# from django.contrib import admin
# from django.urls import path,include
from django.urls.conf import include
from .models import MovieModel
from django.urls import path
from .views import MovieAPIDetail, MovieAPIView, get_movie_detail, movie_list,GenericMovieAPI,MovieAPIViewset

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken import views

router=DefaultRouter()

router.register('movie',MovieAPIViewset,basename='viewset-api')

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('api/',movie_list),

    #path('api/',MovieAPIView.as_view()),
    #path('api/<int:pk>/',get_movie_detail),

    #path('api/<int:id>/',MovieAPIDetail.as_view())

    path('generic-api/',GenericMovieAPI.as_view()),

    path('viewset-api/',include(router.urls)),

    path('get-api-token',views.obtain_auth_token,name='get-api-token')

    #path('generic-api/<int:id>/',GenericMovieAPI.as_view()),



    #path('generic-api/<int:id>/',GenericMovieAPI.as_view())
]