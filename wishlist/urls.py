"""
URL patterns for the wishlist app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('toggle_wishlist/<int:product_id>/', views.wishlist_toggle, name='wishlist_toggle'),
    path('remove_wishlist/<int:product_id>/', views.wishlist_remove, name='wishlist_remove'),
]
