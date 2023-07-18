from django.shortcuts import render, redirect
from django.views.generic import DeleteView
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
    order = Order.objects.filter(user=request.user).latest('id')
    print('order', order)
    return render(request, 'main_app/extension.html', {
        'products': products,
        'order': order
    })


@login_required
def blonde(request):
    return render(request, 'main_app/products/blonde.html')


def products(request):
    return render(request, 'main_app/products.html')


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


def add_to_cart(request, order_id, product_id):
    print('order_id', order_id)
    Order.objects.get(id=order_id).products.add(product_id)
    return redirect('cart')


def remove_from_cart(request, order_id, product_id):
    print('order_id', order_id)
    Order.objects.get(id=order_id).products.remove(product_id)
    return redirect('cart')


@login_required
def cart(request):
    order = Order.objects.filter(user=request.user).latest('id')
    print(order)
    return render(request, "main_app/cart.html", {
        'order': order
    })


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/cart'


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
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
