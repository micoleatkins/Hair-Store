from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Extension(models.Model):
    length = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class Product(models.Model):
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.TextField(max_length=250)
    number = models.CharField(max_length=200)
