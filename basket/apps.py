"""
Django app configuration for the basket app.
"""
from django.apps import AppConfig


class BasketConfig(AppConfig):
    """
    AppConfig for the basket app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
