from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('extensions/', views.extensions, name='extensions_detail'),
    path('customers/', views.customers_index, name='customers_index'),
]
