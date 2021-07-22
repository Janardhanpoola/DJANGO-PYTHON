from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from testapp.models import Employee

from testapp.serializers import EmployeeModelSerializer

from testapp.pagination import EmployeePagination

from testapp.pagination import EmployeePagination1,EmployeePagination2,EmployeeFilteringandsearching


class EmployeeListAPIView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeModelSerializer
   # pagination_class=EmployeePagination 
   # pagination_class=EmployeePagination1
    #pagination_class=EmployeePagination2
    
    pagination_class=EmployeeFilteringandsearching

# 1.# below lines are FILTERING by plain vanilla  filtering
    # def get_queryset(self): #filter based on empname
    #     qs=Employee.objects.all()

    #     name=self.request.GET.get('empname')  #get the empnames of all the records that matches the queryset ..for ex:

    #     if name is not None:

    #         qs=qs.filter(empname__iexact=name)
    #     return qs
        

# 2. below lines are filtering provided by  rest_framework SearchFilter utility

    search_fields=['empname','empid']  #to test this..go to filters in browsable api..this returns the results which contains empname or empid

    #search_fields=['^empid','^empname'] #gives the emp details start with empid specified in filter or ename starting with

    #search_fields=['=empid','=empsal'] #exact match works for only integers

#######line 46 ordering starts

    ordering_fields=['empid','empsal'] #browsable api shows all the fields if ordering_fields is not specified
    #ordering_fields=['empsal']
#####both searching and ordering in one URL : http://127.0.0.1:8000/api/?myfilter=J&myorder=empsal  -->returns emps whose name contains J and ordered by their sal

