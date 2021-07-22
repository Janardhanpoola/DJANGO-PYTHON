from django.db import models

# Create your models here.

class MovieModel(models.Model):
    name=models.CharField(max_length=200)
    duration=models.TimeField()
    genre=models.CharField(max_length=100)
    release_date=models.DateField()


