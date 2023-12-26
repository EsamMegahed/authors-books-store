from django.db import models
from django.urls import reverse
# Create your models here.


class Author(models.Model):
    name = models.CharField(null=False,blank=False,max_length=255)


    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    title = models.CharField(null=False,blank=False,max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book_author',null=False,blank=False)
