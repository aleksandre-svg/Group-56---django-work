from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField()
    desc = models.CharField()
    rating = models.IntegerField()