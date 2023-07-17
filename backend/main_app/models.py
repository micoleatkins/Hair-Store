from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        return total


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('main_app.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    user_Address = models.CharField(max_length=250)
    user_Email = models.EmailField(max_length=70, blank=True, unique=True)
    user_Phone = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return self.name
