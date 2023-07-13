from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Extension(models.Model):
    name = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    number = models.CharField(max_length=10)
    extension = models.ManyToManyField(extension)
    product = models.ManyToManyField(product)

    def __str__(self):
        return self.name


class Product(models.Model):
    quantity = models.IntegerField(default=0)
    price = models.IntegerField('Price')
