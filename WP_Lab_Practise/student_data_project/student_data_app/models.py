from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name