import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','DRF4Pagination.settings')

import django 
django.setup()

from testapp import *
from testapp.models import Employee
from faker import Faker
from random import *

faker=Faker() # creating faker object

def populate(n):
    for i in range(n):
        feno=randint(100,2987)
        fename=faker.name()
        fesal=randint(4566,76542)
        feadr=faker.city()
        emp_data=Employee.objects.get_or_create(empid=feno,empname=fename,empsal=fesal,empadr=feadr)

populate(250)    
