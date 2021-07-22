from django.shortcuts import render

from django.views.generic import View

from django.http import HttpResponse


import json

# Create your views here.

from Emp.models import Emp

from django.core.serializers import serialize

from Emp.mixin import SerailizeMixin

from django.views.decorators.csrf import csrf_exempt #This import is to exempt csrf verifcation at class level(decorator is called just before class)

from django.utils.decorators import method_decorator #This import is to exempt csrf verifcation at class level

from Emp.utils import is_json

from Emp.forms import Empform

@method_decorator(csrf_exempt,name='dispatch')


class EmployeeCRUDCBV(SerailizeMixin,View):

    def get(self,request,*args,**kwargs):
        data=request.body

        valid_json=is_json(data)

        if not valid_json:
           emp_json=json.dumps({'msg':"please provide valid json master1123 "})
           return HttpResponse(emp_json,content_type='application/json',status=400)

        p_data=json.loads(data)

        id=p_data.get('id',None)

        if id is not None:
            try:
                emp=Emp.objects.get(id=id)
            except Emp.DoesNotExist:
                emp=None
            
            if emp is not None:
                emp_json=self.serialize([emp])
                return HttpResponse(emp_json,content_type='application/json',status=200)

            emp_json=json.dumps({'msg':"Emp not found"})
            return HttpResponse(emp_json,content_type='application/json',status=404)

        qs=Emp.objects.all()

        emp_data=self.serialize(qs)

        return HttpResponse(emp_data,content_type='application/json',status=200)          
            
    def post(self,request,*args,**kwargs):
        data=request.body  #it stores the form data(in which the data is already converted to json) sent by partner app.

        if not (is_json(data)):
            json_data=json.dumps({'msg':'please send valid json data'})
            return HttpResponse(json_data,content_type='application/json',status=400)


        emp_py_data=json.loads(data) #converting json to python data to fill form created in python(which accpts only python data)

        form=Empform(emp_py_data)

        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'Resource created successfully'})
            return HttpResponse(json_data,content_type='application/json',status=200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)   



    def put(self,request,*args,**kwargs):
        data=request.body

        valid_json=is_json(data)

        if not valid_json:
           emp_json=json.dumps({'msg':"please provide valid json master "})
           return HttpResponse(emp_json,content_type='application/json',status=400)
        
        p_data=json.loads(data)

        id=p_data.get('id',None) #getting the id if present else None (if id is absent)

        if id is None:
            emp_json=json.dumps({'msg':"id is not provided ...cant update data "})
            return HttpResponse(emp_json,content_type='application/json',status=400)
        
        try:    #id not none....get the details of the emp of given id 
            emp=Emp.objects.get(id=id)
        except Emp.DoesNotExist:
            emp=None
        
        if emp is None:
            emp_json=json.dumps({'msg':"emp does not exist ..cant update "})
            return HttpResponse(emp_json,content_type='application/json',status=400)
        
        p_data=json.loads(data) #converting update data from partner app to python data

        original_data={   #getting the original data of the emp of specific id 
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadr': emp.eadr
        }

    
        original_data.update(p_data) #updating dictionary with the latest values provided from partner app.

        form=Empform(original_data,instance=emp)

        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'Resource updated successfully'})
            return HttpResponse(json_data,content_type='application/json',status=200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)       

    def delete(self,request,*args,**kwargs):
        data=request.body

        p_data=json.loads(data)

        id=p_data.get('id',None)

        if id is None:
            emp_json=json.dumps({'msg':"id is not provided ...cant delete data "})
            return HttpResponse(emp_json,content_type='application/json',status=400)
        
        try:    #id not none....get the details of the emp of given id 
            emp=Emp.objects.get(id=id)
        except Emp.DoesNotExist:
            emp=None
        
        if emp is None:
            emp_json=json.dumps({'msg':"emp does not exist ..cant delete "})
            return HttpResponse(emp_json,content_type='application/json',status=400)  

        status,deleted_item=emp.delete()  #query set method...it contains a tuple with 2 values ....1st is status code ..2nd deleted item

        if status==1:
            emp_json=json.dumps({'msg':'Employee deleted successfully'})
            return HttpResponse(emp_json,content_type='application/json')
        emp_json=json.dumps({'msg':'unable to delete plz try again '})
        return HttpResponse(emp_json,content_type='application/json')  
        







        

        




    


@method_decorator(csrf_exempt,name='dispatch')
class EmpCBV(SerailizeMixin,View):

    def get(self,request,id,*args,**kwargs):

        try:

            emp=Emp.objects.get(id=id)
        except Emp.DoesNotExist:

            emp_json=json.dumps({'msg':"Employee info does not exists"})
            return HttpResponse(emp_json,content_type='application/json',status=404)
        else:
            emp_json=self.serialize([emp]) #if you want convert large fields dict to json (serialize is used)..1st is type you want to convert,2nd arg is queryset

                                            #emp_json=serialize('json',[emp,],fields=('eno','ename')) #if you want to restrict no. of fields use fields arg
                                            #   emp_data={
                                            #       'eno':emp.eno,
                                            #       'ename':emp.ename,
                                            #       'esal':emp.esal,
                                            #       'eadr':emp.eadr
                                            #   }

                                            #   emp_json=json.dumps(emp_data)

            return HttpResponse(emp_json,content_type='application/json',status=200)

    def put(self,request,id,*args,**kwargs):
        try:
            emp=Emp.objects.get(id=id)
        except Emp.DoesNotExist:
            emp=None  

        if emp is None: #if id not present 
            emp_json=json.dumps({'msg':'Requested resource not found'})
            return HttpResponse(emp_json,content_type='application/json',status=400)            

        update_data=request.body  #json data from partner app

        if not is_json(update_data):
            emp_json=json.dumps({'msg':'please specify valid json'})
            return HttpResponse(emp_json,content_type='application/json')

        p_data=json.loads(update_data) #converting update data from partner app to python data

        original_data={   #getting the original data of the emp of specific id 
            'eno': emp.eno,
            'ename': emp.ename,
            'esal': emp.esal,
            'eadr': emp.eadr
        }

    
        original_data.update(p_data) #updating dictionary with the latest values provided from partner app.

        form=Empform(original_data,instance=emp)

        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'Resource updated successfully'})
            return HttpResponse(json_data,content_type='application/json',status=200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)           

    def delete(self,request,id,*args,**kwargs):
        try:
            emp=Emp.objects.get(id=id)
        except Emp.DoesNotExist:
            emp_json=json.dumps({'msg':'Employee does not exist..unable to perform deletion'})
            return HttpResponse(emp_json,content_type='application/json',status=400)

        else:

            status,deleted_item=emp.delete()  #query set method...it contains a tuple with 2 values ....1st is status code ..2nd deleted item
            if status==1:
                emp_json=json.dumps({'msg':'Employee deleted successfully'})
                return HttpResponse(emp_json,content_type='application/json')
            emp_json=json.dumps({'msg':'unable to delete plz try again '})
            return HttpResponse(emp_json,content_type='application/json')



@method_decorator(csrf_exempt,name='dispatch')  #This is to exempt csrf verifcation at class level

class EmpCBVall(SerailizeMixin,View):

    def get(self,request,*args,**kwargs):
        qs=Emp.objects.all()    

        emp_json=self.serialize(qs)
        return HttpResponse(emp_json,content_type='application/json')
    
    def post(self,request,*args,**kwargs):
        data=request.body  #it stores the form data(in which the data is already converted to json) sent by partner app.

        if not (is_json(data)):
            json_data=json.dumps({'msg':'please send valid json data'})
            return HttpResponse(json_data,content_type='application/json',status=400)


        emp_py_data=json.loads(data) #converting json to python data to fill form created in python(which accpts only python data)

        form=Empform(emp_py_data)

        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg':'Resource created successfully'})
            return HttpResponse(json_data,content_type='application/json',status=200)
        if form.errors:
            json_data=json.dumps(form.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)   


            

        


