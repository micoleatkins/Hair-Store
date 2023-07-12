from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def extensions(request):
    return render(request, 'main_app/extensions.html')


def products(request):
    return render(request, 'main_app/products.html')


def mink_detail(request):
    return render(request, 'main_app/mink_detail.html')


def closure_detail(request):
    return render(request, 'main_app/closure_detail.html')


def blonde_detail(request):
    return render(request, 'main_app/blonde_detail.html')


def customers_index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        'customers': customers
    })
