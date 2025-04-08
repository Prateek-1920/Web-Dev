from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    email = models.EmailField()    
    
    def __str__(self):
        return self.name
    
