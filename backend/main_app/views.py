from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Product


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def extension(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'main_app/extension.html', {
        'products': products
    })


def blonde(request):
    return render(request, 'main_app/products/blonde.html')


def products(request):
    return render(request, 'main_app/products.html')


def mink_detail(request):
    return render(request, 'main_app/products/mink_detail.html')


def closure_detail(request):
    return render(request, 'main_app/products/closure_detail.html')


def edge_detail(request):
    return render(request, 'main_app/products/edge_detail.html')


def oil_detail(request):
    return render(request, 'main_app/products/oil_detail.html')


def mask_detail(request):
    return render(request, 'main_app/products/mask_detail.html')


def checkout(request):
    return render(request, 'main_app/checkout.html')


def getCart(request):
    product = Product.objects.get(id=product_id)
    return render(request, 'main_app/cart.html')


def cart(request, orderitems_id):
    orderitems = Orderitems.objects.get(id=orderitems_id)
    print(product)
    return render(request, 'main_app/cart.html', {
        'orderitems': orderitems,

    })


def customers_index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        'customers': customers
    })
