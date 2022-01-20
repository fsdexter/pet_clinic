from curses import ACS_GEQUAL
from turtle import setx
from unicodedata import name
from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(max_length=3)
    dni =models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250)
    
class Pets(models.Model):
    id = models.IntegerField(max_length=150)
    age = models.IntegerField(max_length=3)
    name = models.CharField(max_length=150)
    species = models.CharField(max_length=150)
    sex = models.CharField(max_length=10)
    slug = models.SlugField(max_length=250)
