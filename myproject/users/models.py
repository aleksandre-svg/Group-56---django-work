from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField()
    is_current_user = models.BooleanField(default=0)