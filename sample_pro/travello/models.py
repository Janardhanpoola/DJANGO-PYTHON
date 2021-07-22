from django.db import models

# Create your models here.

class destination(models.Model):
    #id: int
    #name: str
    #price: int
    #desc : str
    #img : str
    #offer : bool

    name=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)

