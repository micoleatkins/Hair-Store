from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=250)
    user_Address = models.CharField(max_length=250)
    user_Email = models.EmailField(max_length=70, blank=True, unique=True)
    user_Number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Extension(models.Model):
    name = models.CharField(max_length=150)
    length = models.IntegerField(null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mink_detail', kwargs={'pk': self.id})


class Product(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
