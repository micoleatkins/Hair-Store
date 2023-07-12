from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('extensions/', views.extensions, name='extensions_detail'),
    path('mink_detail/', views.mink_detail, name='mink_detail'),
    path('closure_detail/', views.closure_detail, name='closure_detail'),
    path('blonde_detail/', views.blonde_detail, name='blonde_detail'),
    path('products/', views.products, name='products_detail')
]
