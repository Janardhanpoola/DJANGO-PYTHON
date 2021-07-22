from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def emp_info(request):
    emp={'emp_no':100,
        'emp_name':"raj",
        'emp_sal':1000,
        'emp_adr':"Mumbai"
    }

    Emp_no=emp['emp_no']
    Emp_name=emp['emp_name']
    Emp_sal=emp['emp_sal']
    Emp_adr=emp['emp_adr']




    return render(request,"emp.html",{'Emp_no':Emp_no,'Emp_name':Emp_name,'Emp_sal':Emp_sal,'Emp_adr':Emp_adr})

import json

def emp_json(request):

    emp={'emp_no':100,
        'emp_name':"raj",
        'emp_sal':1000,
        'emp_adr':"Mumbai"
    }

    json_emp=json.dumps(emp)

    return HttpResponse(json_emp,content_type='application/json')


from django.views import View
from django.http import JsonResponse

from Edata.mixin import HttpResponseMixin

class JsonCBV(HttpResponseMixin,View):

    def get(self,request,*args,**kwargs):

        content={'msg':'This is get'}
        json_data=json.dumps(content)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):

        content={'msg':'This is Post'}
        json_data=json.dumps(content)
        return self.render_to_http_response(json_data)

    


