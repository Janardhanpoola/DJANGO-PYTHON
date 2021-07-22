from django.db import models

# Create your models here.

class Track(models.Model):
    trackname=models.CharField(max_length=100)
    Albumid=models.IntegerField()
    MediaTypeid=models.IntegerField()
    GenreId=models.IntegerField()
    Composer=models.CharField(max_length=200,null=True)
    Milllisecs=models.IntegerField()
    Bytes=models.IntegerField()
    unitprice=models.FloatField()
