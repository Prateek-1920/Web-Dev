from django.db import models

class Bill(models.Model):
    name = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    # date = models.DateField()
    
    def __str__(self):
        return self.name