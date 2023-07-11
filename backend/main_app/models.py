from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.TextField(max_length=250)
    number = models.CharField(max_length=200)

# Create your models here.
