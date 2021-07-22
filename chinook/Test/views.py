from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

from .models import Track

from .serializer import TrackModelSerializer

# class TrackListAPIView(ListAPIView): #used to get data from browsable API
#     queryset=Track.objects.all()  #queryset is predefined
#     serializer_class=TrackModelSerializer #serializer_class is predefined



class TrackListCreateAPIView(ListCreateAPIView):
    queryset=Track.objects.all()
    serializer_class=TrackModelSerializer
    def get_queryset(self):  #to perform search operations based on particular fields..use get_queryset predefined method

        qs=Track.objects.all()

        name=self.request.GET.get('trackname')
        genre=self.request.GET.get('GenreId')

        if name is not None :
            qs=qs.filter(trackname__icontains=name)
        
        if genre is not None:
            qs=qs.filter(GenreId__iexact=genre)

        return qs      
 

class TrackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Track.objects.all()
    serializer_class=TrackModelSerializer