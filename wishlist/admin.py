from django.contrib import admin

from .models import Wishlist

class WishlistProductInline(admin.TabularInline):
    model = Wishlist.products.through

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    inlines = [WishlistProductInline,]

    list_display = ['user_profile',]
