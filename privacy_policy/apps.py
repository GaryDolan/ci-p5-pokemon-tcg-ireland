"""
Django app configuration for the privacy_policy app.
"""
from django.apps import AppConfig


class PrivacyPolicyConfig(AppConfig):
    """
    AppConfig for the privacy_policy app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'privacy_policy'
