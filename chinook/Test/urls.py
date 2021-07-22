from django.urls import path,include,re_path


from . import views
urlpatterns = [
    #path('api/',views.TrackListAPIView.as_view()),
    path('api/',views.TrackListCreateAPIView.as_view()),
    re_path(r'^api/(?P<pk>\d+)/$',views.TrackRetrieveUpdateDestroyAPIView.as_view())
]