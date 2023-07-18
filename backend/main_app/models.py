from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.user.username} - {self.products.name}'

    def get_total_price(self):
        products = self.products.all()
        print(products)
        total = products.aggregate(sum=Sum('price'))['sum']
        return total


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    user_Address = models.CharField(max_length=250)
    user_Email = models.EmailField(max_length=70, blank=True, unique=True)
    user_Phone = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return self.name
