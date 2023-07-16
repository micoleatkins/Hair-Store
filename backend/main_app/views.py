from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Order


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def extension(request):
    products = Product.objects.all()
    return render(request, 'main_app/extension.html', {
        'products': products
    })


@login_required
def blonde(request):
    return render(request, 'main_app/products/blonde.html')


def products(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'main_app/products.html', {'products': product})


@login_required
def mink_detail(request):
    return render(request, 'main_app/products/mink_detail.html')


@login_required
def closure_detail(request):
    return render(request, 'main_app/products/closure_detail.html')


@login_required
def edge_detail(request):
    return render(request, 'main_app/products/edge_detail.html')


@login_required
def oil_detail(request):
    return render(request, 'main_app/products/oil_detail.html')


@login_required
def mask_detail(request):
    return render(request, 'main_app/products/mask_detail.html')


@login_required
def checkout(request):
    return render(request, 'main_app/checkout.html')


@login_required
def getCart(request):
    product = Product.objects.get(id=product_id)
    return render(request, 'main_app/cart.html')


@login_required
def cart(request, orderitems_id):
    orderitems = Orderitems.objects.get(id=orderitems_id)
    print(product)
    return render(request, 'main_app/cart.html', {
        'orderitems': orderitems,

    })


@login_required
def customers_index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        'customers': customers
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
