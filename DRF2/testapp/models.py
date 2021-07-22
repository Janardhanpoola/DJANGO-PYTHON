from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):

    empid=models.IntegerField()
    empname=models.CharField(max_length=64)
    empsal=models.FloatField()
    empadr=models.CharField(max_length=64)
