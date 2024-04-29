"""
URL patterns for the privacy_policy app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

]
