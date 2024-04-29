"""
Admin configurations for the profiles app
"""
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the profile model
    """
    list_display = [
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_country',
        'default_postcode',
        'default_county'
    ]
    list_filter = ['default_town_or_city', 'default_county', 'default_country']
    search_fields = ['user', 'default_phone_number']
