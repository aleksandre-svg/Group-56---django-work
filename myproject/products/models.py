from django.db import models
from users.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField()
    price = models.FloatField()
    desc = models.CharField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title