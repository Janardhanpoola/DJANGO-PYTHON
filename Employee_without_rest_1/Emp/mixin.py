from Emp import views

from django.core.serializers import serialize

import json

class SerailizeMixin(object): 

    def serialize(self,qs): #converting all the fields of employee to json
        emp_json=serialize('json',qs)  #if you want convert large fields dict to json (serialize is used)..1st us type you want to convert,2nd arg is queryset
        pdict=json.loads(emp_json) # converts json to python dict
        final_list=[]
        for obj in pdict:
            edata=obj['fields']
            final_list.append(edata)

        emp_json=json.dumps(final_list) #converts dict to json 

        return emp_json       

