from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # specified that product id is an int so when add is called it wont mistake it for products/add(thinking add is an id)
    # if we didnt add would match this and because its first in the list it would be called
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    
]
