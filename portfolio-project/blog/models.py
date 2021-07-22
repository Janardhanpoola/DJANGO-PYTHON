from django.db import models

# Create your models here.
#create blog model

class Blog(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateField()
    body=models.TextField(max_length=200)
    image=models.ImageField(upload_to="images")

    def time(self):
        return self.pub_date.strftime(" %d %b %Y")
    
    def __str__(self):  #displays the particular object in django-admin when clicked on blogs
        return self.title