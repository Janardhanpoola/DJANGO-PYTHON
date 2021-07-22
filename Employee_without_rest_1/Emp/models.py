from django.db import models

# Create your models here.

class Emp(models.Model):

    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eadr=models.CharField(max_length=64)
