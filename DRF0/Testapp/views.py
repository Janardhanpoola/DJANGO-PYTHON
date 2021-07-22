from django.shortcuts import render

from django.views.generic import View

import io

from rest_framework.renderers import JSONRenderer

from Testapp.models import Employee

from Testapp.serializers import EmployeeSerializer

from rest_framework.parsers import JSONParser

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator #This import is to exempt csrf verifcation at class level


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')


class EmployeeCRUDCBV(View):

    def get(self,request,*args,**kwargs):

        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data) #converting to stream

        print(stream)

        p_data=JSONParser().parse(stream) #converting to python data

        id=p_data.get('id',None)

        if id is not None:
            try:
                emp=Employee.objects.get(id=id) #qs 
            
            except Employee.DoesNotExist:
                msg={'msg':'id not found'}
                json_data=JSONRenderer().render(msg)
                return HttpResponse(json_data,content_type='application/json')
            
            eserializer=EmployeeSerializer(emp)

            json_data=JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json')

        

        qs=Employee.objects.all()
        eserializer=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data,content_type='application/json') 

    

    def post(self,request,*args,**kwargs):
        json_data=request.body

        stream=io.BytesIO(json_data)

        p_data=JSONParser().parse(stream)

        serailizer=EmployeeSerializer(data=p_data)

        if serailizer.is_valid():
            serailizer.save()# it will call create mtd defined in serializers.py
            msg={'msg':'resource create successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
       
        json_data=JSONRenderer().render(serailizer.errors) # if serializers has errors
        return HttpResponse(json_data,content_type='application/json',status=400)


    def put(self,request,*args,**kwargs):

        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id')

        emp=Employee.objects.get(id=id)
        serailizer=EmployeeSerializer(emp,data=p_data,partial=True)  #updates emp with the p_data....partial allows us to update partial updation
        # if partial is not specified : it o/p as  {'eno': ['This field is required.'], 'ename': ['This field is required.']}400
        if serailizer.is_valid():
            serailizer.save() #it will call update mtd defined in views.py
            msg={'msg':"resource updated"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serailizer.errors) # if serializers has errors
        return HttpResponse(json_data,content_type='application/json',status=400)            

        
    def delete(self,request,*args,**kwargs):

        json_data=request.body
        stream=io.BytesIO(json_data)
        p_data=JSONParser().parse(stream)
        id=p_data.get('id')

        emp=Employee.objects.get(id=id)

        emp.delete()         

        msg={'msg':"resource deleted"}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')




        










