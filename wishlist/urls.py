from django.urls import path
from . import views

urlpatterns = [
    path('toggle_wishlist/<int:product_id>', views.wishlist_toggle, name='wishlist_toggle'),

]