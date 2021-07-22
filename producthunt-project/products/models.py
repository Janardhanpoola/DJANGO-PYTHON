from django.db import models

from django.contrib.auth.models import User

# Create your models here.

#product class

class Product(models.Model):
#title
    title=models.CharField(max_length=200)
#url
    url=models.TextField()
#image
    pic=models.ImageField(upload_to='pictures/')
#icon
    icon=models.ImageField(upload_to='pictures/')
#pub_date
    pub_date=models.DateField()
#body
    body=models.TextField()
#votes total
    votes_total=models.IntegerField(default=1)

#hunter
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)  #stroes the id of the user, if user is deleted ,product is deleted.(i.e on_delete=CASCADE)

def summary(self):
    return self.body[:100]