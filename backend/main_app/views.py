from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def extensions(request):
    return render(request, 'extensions.html')
