from django.db import models

# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=54)
    esal=models.FloatField()
    eadr=models.CharField(max_length=54)
