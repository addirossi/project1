from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150)