from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.viewsets import ViewSet

from Testapp.serializer import NameSerializer

# Create your views here.

class TestAPIView(APIView):
    
    def get(self,request,*args,**kwargs):
        colors=['yellow','black','red']

        return Response({'msg':'Happy Christmas','colors':colors}) #Response will automatically convert python data to json

    
    def post(self,request,*args,**kwargs):
        
        serializer=NameSerializer(data=request.data) # the data posted from browsable API will be stored in serializer

        if serializer.is_valid():
            name=serializer.data.get('name')

            msg=f'hello {name} ...welcome to browsable API'

            return Response({'msg':msg})

        return Response(serializer.errors,status=400)

    def put(self,request,*args,**kwargs):

        return Response({'msg':"hello from put"})

    def delete(self,request):

        return Response({"msg":"from delete"})


#-------------------------------

#in viewsets we dont need to map views in url patttern.
# Routers (DefaultRouter) will automatically map views to urls ....see urls.py for more info

#  list()     -->similar to get in APIView
#  retrieve()-->to get only particular item
#  create() --->similar to post in APIView
#  update()---> similar to put in APIView
#  partial_update() -->similar to patch() in APIView
#  destroy() -->similar to delete() 

class TestViewSet(ViewSet):
    pass

    def list(self,request): #similar to get
        colors=['yellow','black','red']
        return Response({'msg':'Happy Christmas','colors':colors})    


    def create(self,request): #similar to post

        serializer=NameSerializer(data=request.data) 

        if serializer.is_valid():
            name=serializer.data.get('name')

            msg=f'hey {name} how you?'

            return Response({'msg':msg})
        return Response(serializer.errors)    
    
    def retrieve(self,request,pk=None):  #need to specify pk when user requests a particular recordhttp://127.0.0.1:8000/test-view-set/1/

        msg={'msg':'this is to fetch a particular record'}

        return Response({'msg':msg})

    def update(self,request,pk=None): #pk must..

        msg={'msg':'this is to update '}

        return Response({'msg':msg})

    def destroy(self,request,pk=None): #pk must
        msg={'msg':'records deleted '}

        return Response({'msg':msg})





    




