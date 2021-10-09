from django.db import models

# Create your models here.

class Target(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=64)

class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    contents = models.CharField(max_length=10000)
    created_date = models.DateField(auto_now=True)