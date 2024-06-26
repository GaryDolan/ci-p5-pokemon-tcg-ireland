"""
URL patterns for the products app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    # specified that product id is an int so when add is called it wont
    # mistake it for products/add (thinking add is an id) if we didn't
    # add would match this and because its first in the list it would be called
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path(
        'delete_review/<int:review_id>/',
        views.delete_review,
        name='delete_review'
    ),

]
