from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('extension/', views.extension, name='extension'),
    path('products/mink_detail/', views.mink_detail, name='mink_detail'),
    path('products/closure_detail/', views.closure_detail, name='closure_detail'),
    path('products/blonde/', views.blonde, name='blonde'),
    path('products/', views.products, name='products_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/edge_detail/', views.edge_detail, name='edge_detail'),
    path('products/oil_detail/', views.oil_detail, name='oil_detail'),
    path('products/mask_detail/', views.mask_detail, name='mask_detail'),
    path('cart/<int:product_id>/', views.cart, name='cart'),
    path('cart/<int:pk>/', views.getCart, name='cart'),
]
