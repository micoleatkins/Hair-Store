from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('customers/', views.customers_index, name='index'),
    path('extension/', views.extension, name='extension'),
    path('products/mink_detail/', views.mink_detail, name='mink_detail'),
    path('products/closure_detail/', views.closure_detail, name='closure_detail'),
    path('products/blonde/', views.blonde, name='blonde'),
    path('products/', views.products, name='products_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/edge_detail/', views.edge_detail, name='edge_detail'),
    path('products/oil_detail/', views.oil_detail, name='oil_detail'),
    path('products/mask_detail/', views.mask_detail, name='mask_detail'),
    path("cart/", views.cart, name="cart"),
    path('cart/<int:pk>/delete',
         views.ProductDelete.as_view(), name='product_delete'),
    path("cart/<int:order_id>/add_to_cart/<int:product_id>",
         views.add_to_cart, name="add_to_cart"),
    path("cart/<int:order_id>/remove_from_cart/<int:product_id>",
         views.remove_from_cart, name="remove_from_cart"),
    path('accounts/signup/', views.signup, name='signup'),
]
