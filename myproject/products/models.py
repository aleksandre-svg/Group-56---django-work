from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField()
    price = models.FloatField()
    desc = models.CharField()
    rating = models.IntegerField()
    user = models.IntegerField()
    
    def __str__(self):
        return self.title