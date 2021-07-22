from django.db import models

# Create your models here.

class Student(models.Model):
    Fname=models.CharField(max_length=200,null=True)
    Lname=models.CharField(max_length=200,null=True)
    Age=models.IntegerField(null=True)
    Class=models.IntegerField(null=True)
    Section=models.CharField(max_length=200,null=True)
    Maths=models.IntegerField(null=True)
    Physics=models.IntegerField(null=True)
    Chemistry=models.IntegerField(null=True)
    Biology=models.IntegerField(null=True)	
    Stu_ID=models.IntegerField(null=True)
    Email_ID=models.EmailField(max_length=200,null=True)

