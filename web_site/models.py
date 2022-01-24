
from django.db import models

#Create your models here.

class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    dni =models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    
class Pets(models.Model):
    id = models.IntegerField(primary_key=True)
    slug = models.SlugField(max_length=250)
    age = models.IntegerField()
    name = models.CharField(max_length=150)
    species = models.CharField(max_length=150)
    sex = models.CharField(max_length=10)
