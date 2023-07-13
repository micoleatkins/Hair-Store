from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('extensions/', views.extensions, name='extensions_detail'),
    path('mink_detail/', views.mink_detail, name='mink_detail'),
    path('closure_detail/', views.closure_detail, name='closure_detail'),
    path('blonde/', views.blonde, name='blonde'),
    path('products/', views.products, name='products_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('edge_detail/', views.edge_detail, name='edge_detail'),
    path('oil_detail/', views.oil_detail, name='oil_detail'),

]
