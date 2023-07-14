from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from delocate.fuse import fuse_wheels
import uuid

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(null=False, blank=False)
    picture = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="orderitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name


class Customer(models.Model):
    username = models.CharField(max_length=250)
    user_Address = models.CharField(max_length=250)
    user_Email = models.EmailField(max_length=70, blank=True, unique=True)
    user_Phone = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return self.name
