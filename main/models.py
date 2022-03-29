import email
from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)

class Model2(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)