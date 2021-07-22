import requests

BASE_URL="http://127.0.0.1:8000/"

ENDPOINT="emp_json_cbv"

res=requests.get(BASE_URL+ENDPOINT)

print(type(res))

data=res.json()

print(data)

print(type(data))

