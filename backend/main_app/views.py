from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Product, Order, OrderItem, Customer


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def extension(request):
    return render(request, 'main_app/extension.html')


def blonde(request):
    return render(request, 'main_app/blonde.html')


def products(request):
    return render(request, 'main_app/products.html')


def mink_detail(request):
    return render(request, 'main_app/mink_detail.html')


def closure_detail(request):
    return render(request, 'main_app/closure_detail.html')


def edge_detail(request):
    return render(request, 'main_app/edge_detail.html')


def oil_detail(request):
    return render(request, 'main_app/oil_detail.html')


def mask_detail(request):
    return render(request, 'main_app/mask_detail.html')


def checkout(request):
    return render(request, 'main_app/checkout.html')


def cart(request):
    return render(request, 'main_app/cart.html')


def customers_index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        'customers': customers
    })
