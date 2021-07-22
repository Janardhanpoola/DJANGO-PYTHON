from django.db import models

# Create your models here.

class Job(models.Model):  
    image=models.ImageField(upload_to='images')  #location where img needs to be stored within the media folder
    summary=models.CharField(max_length=200) # Brief description  about job

