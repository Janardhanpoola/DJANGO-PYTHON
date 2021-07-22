from django.db.models.query import ModelIterable
from django.shortcuts import render

from .serializers import MovieSerializer

from .models import MovieModel

#from rest_framework.renderers import JsonRenderer


from rest_framework.parsers import JSONParser

from rest_framework.renderers import JSONRenderer


from django.http import JsonResponse,HttpResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from rest_framework.response import Response

#from rest_framework.generics import ListModelMixin

from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView

from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin

from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated

#####################
#Generic APIViews
####################

class GenericMovieAPI(GenericAPIView,ListModelMixin,CreateModelMixin,UpdateModelMixin):
    serializer_class=MovieSerializer
    queryset=MovieModel.objects.all()

    lookup_field='id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:

            return self.list(request)

    def post(self,request):
        return self.create(request)
    
    def put(self,request):
        
        return self.update(request,id)


###########
#Viewsets(ModelViewsets)
###########


class MovieAPIViewset(viewsets.ModelViewSet):

    serializer_class=MovieSerializer
    queryset=MovieModel.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


    




###########
#CLASS BASED API VIEWS 
################

class MovieAPIView(APIView):
    def get(self,request):
        movies=MovieModel.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

class MovieAPIDetail(APIView):

        def get(self,request,id=None):
            try:
                movie=MovieModel.objects.get(id=id)
            except MovieModel.DoesNotExist:
                msg={"msg":"requested resource doesnot exist"}
                return Response(msg,status=404)
            serializer=MovieSerializer(movie)
            return Response(serializer.data,status=200)

        def put(self,request,id=None):
            movie=MovieModel.objects.get(id=id)

            serializer=MovieSerializer(movie,data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=200)
            else:
                return Response(serializer.errors,status=400)
            
        def delete(self,request,id=None):
            movie=MovieModel.objects.get(id=id)
            movie.delete()
            return Response(status=204)


        






############FUNCTION BASED VIEWS

######################



@api_view(['GET','POST','PUT','DELETE'])
# Create your views here.
def movie_list(request):

    if request.method=='GET':
        movies=MovieModel.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        #data=JSONParser().parse(request) #to parse our data
        serializer=MovieSerializer(data=request.data)#serializing it

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)


    
   

    

@api_view(['GET','PUT','DELETE'])
def get_movie_detail(request,pk):
    try:
        movie=MovieModel.objects.get(id=pk)
    except MovieModel.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer=MovieSerializer(movie)
        return Response(serializer.data,status=200)

    elif request.method=='PUT':
        data=JSONParser().parse(request) #parsing the data
        serializer=MovieSerializer(movie,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

    elif request.method=='DELETE':
        movie.delete()
        return HttpResponse(status=204)

































