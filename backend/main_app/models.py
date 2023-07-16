from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(null="False", blank="False")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name="items")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'order_id': self.id})

    def get_cost(self):
        return self.product.price * self.quantity


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    user_Address = models.CharField(max_length=250)
    user_Email = models.EmailField(max_length=70, blank=True, unique=True)
    user_Phone = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return self.name
