from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def extensions(request):
    return render(request, 'extensions.html')


def customers_index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        'customers': customers
    })
