from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Issue(models.Model):
    borrower = models.ForeignKey(Borrower,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    
    # def __str__(self):
    #     return self.borrower
    