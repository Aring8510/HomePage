from django.db import models

# Create your models here.

class Target(models.Model):
    name = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)

 