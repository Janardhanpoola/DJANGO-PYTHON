import requests
import json
from pprint import pprint
BASE_URL="http://127.0.0.1:8000/"

ENDPOINT="api/"

def get_resource(id=None):
    data={}
    if id is not None:
        
        data={
            'id':id
        }

    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    pprint(resp.status_code)
    pprint(resp.json())


def create_resource():
    data={

        'eno':55,
        'ename': 'janaa',
        'esal':4500,
        'eadr':'jodhpura'

    }

    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.json())
    print(resp.status_code)


def update_resource(id):
    data={

        'id':id,
        'esal':19800,
        'eadr':'KKD'

    }

    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.json())
    print(resp.status_code)


def delete_resource(id):
    data={
        'id':id
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.json())
    print(resp.status_code)    

#delete_resource(10)

#update_resource(1)

create_resource()


#get_resource()

