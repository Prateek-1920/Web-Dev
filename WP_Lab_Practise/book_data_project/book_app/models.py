from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    