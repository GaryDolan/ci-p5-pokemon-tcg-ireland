"""
Admin configurations for the wishlist app
"""
from django.contrib import admin

from .models import Wishlist


class WishlistProductInline(admin.TabularInline):
    """
    Inline model admin for managing products in a wishlist
    """
    model = Wishlist.products.through


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the wishlist model
    """
    inlines = [WishlistProductInline, ]

    list_display = ['user_profile', ]
