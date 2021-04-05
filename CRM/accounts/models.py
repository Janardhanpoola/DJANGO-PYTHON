from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# customer--> orders(1 to many relationship)
#product-> orders (1 to many relationship) for this scenario
# Tags-->products (Many to Many)

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)  #creating a user profile ....one User has one customer
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    profile_pic=models.ImageField(default='logo.png',null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name=models.CharField(max_length=100)     
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    CAT=[('Indoor','Indoor'),
    ('Outdoor','Outdoor')]
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    category=models.CharField(max_length=200,null=True,choices=CAT)
    description=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.name)



class Order(models.Model):
    STATUS=[('Pending','Pending'),('Out for delivery','Out for delivery'),('Delivered','Delivered')]

    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)

    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)

    note=models.CharField(max_length=100,null=True)

    def filter_date(self):
        return self.date_created.strftime("%d-%m-%Y")
    
    def __str__(self):
        return str(self.product.name)
    

