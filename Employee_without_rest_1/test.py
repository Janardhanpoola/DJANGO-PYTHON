import requests
from pprint import pprint

import json

BASE_URL="http://127.0.0.1:8000/"

ENDPOINT='api/'
# def get_resource1(id):


#     resp=requests.get(BASE_URL+ENDPOINT+id)

#     print(resp.status_code)

#     print(resp.json())


def get_resource(id=None):

    data={}
    if id is not None:
        data={
            'id':id
        }
    emp_json=json.dumps(data)
    resp=requests.get(BASE_URL+ENDPOINT,data=emp_json)
    print(resp)
    pprint(resp.status_code)
    pprint(resp.json())



def create_resource():
    new_emp={

        'eno':33230,
        'ename':"venkatesh",
        'esal':10123,
        'eadr':'PUR'
    }

    emp_json=json.dumps(new_emp)
    resp=requests.post(BASE_URL+ENDPOINT,data=emp_json) #data should be of json format

    print(resp.status_code)
    print(resp.json())
    print(type(resp.json()))


# def update_resource(id):
#     new_emp={

#         'ename':"pawan",
#         'esal': 40000
       
#     }

#     emp_json=json.dumps(new_emp)
#     resp=requests.put(BASE_URL+ENDPOINT+str(id)+"/",data=emp_json) #data should be of json format

#     print(resp.status_code)
#     print(resp.json())

def update_resource(id):
    new_emp={
        'id': id,
        'ename': "pawan",
        'esal': 50000      
    }

    emp_json=json.dumps(new_emp)
    resp=requests.put(BASE_URL+ENDPOINT,data=emp_json) #data should be of json format

    print(resp.status_code)
    print(resp.json())




def delete_resource(id=None):

    data={}

    if id is not None:
        data={

            'id' : id
        }

    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data)) 

    print(resp.status_code)
    print(resp.json())



#get_resource(10)




#delete_resource(10)

#update_resource(10)

#create_resource()

#get_resource(6)


#id=input("enter resource id:   ")

#get_resource1(id)


