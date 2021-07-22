from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=45)
    subject=models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Book(models.Model):

    isbn=models.CharField(max_length=45)
    title=models.CharField(max_length=67)
    pub_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books_by_author')  #on_delete cascade means if the info in author table is deleted then corresponding info in books table will also be deleted
                                                                                               #...related_name is used to link models.
    def __str__(self):
        return self.title