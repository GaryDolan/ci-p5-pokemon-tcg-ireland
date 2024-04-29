"""
Django app configuration for the wishlist app.
"""
from django.apps import AppConfig


class WishlistConfig(AppConfig):
    """
    AppConfig for the wishlist app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wishlist'
