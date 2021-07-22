from django.shortcuts import render

from rest_framework.views import APIView

from testapp.serializer import EmployeeModelSerializer
from testapp.models import EmployeeInfo

from rest_framework.response import Response

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
# we can get the items in the database using APIVIew class and ListAPIView class

#ListAPIView is more of a shorcut than APIView. code from lines 18 to 22 are implementation of get using APIView class


# class EmployeeListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=EmployeeInfo.objects.all()
#         serializer=EmployeeModelSerializer(qs,many=True)
#         return Response(serializer.data)

 
class EmployeeListAPIView(ListAPIView): #used to get data from browsable API
    queryset=EmployeeInfo.objects.all()  #queryset is predefined
    serializer_class=EmployeeModelSerializer #serializer_class is predefined

    def get_queryset(self):  #to perform search operations based on particular fields..use get_queryset predefined method

        #  use query string in google url..for ex: http://127.0.0.1:8000/api/?empname=mani
        qs=EmployeeInfo.objects.all()

        name=self.request.GET.get('empname') #field you want to search for....self.request.GET will contain all the data containing key,value pairs.. and (.get) is used to get value of the specified field

        address=self.request.GET.get('empadr')
        
        if name is not None :
            qs=qs.filter(empname__icontains=name) # icontains searches if pattern contains....iexact matches the exact string
            

        if address is not None:
            qs=qs.filter(empadr__icontains=address) #gives address which has given input in that for ex:http://127.0.0.1:8000/api/?empadr=b


        return qs # if query string(?ename=mani) is not provided..all the fields will be displayed i.e http://127.0.0.1:8000/api/

 



class EmployeeCreateAPIView(CreateAPIView): #used to post data using browsable API
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer
    



class EmployeeRetrieveAPIView(RetrieveAPIView):  #to retrieve a particular record..you need to specify 'pk' field in URL pattern

    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer


class EmployeeUpdateAPIView(UpdateAPIView):
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer

class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer

class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer

class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=EmployeeInfo.objects.all()
    serializer_class=EmployeeModelSerializer
 

############Mixin concept


# from rest_framework import mixins

# class EmployeeListCreateAPIViewM(mixins.CreateModelMixin,ListAPIView):
#     queryset=EmployeeInfo.objects.all()
#     serializer_class=EmployeeModelSerializer
#     def post(request,*args,**kwargs):
#         return self.post(request,*args,**kwargs)











