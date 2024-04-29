"""
Admin configurations for the products app
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product, Category, CardSet, Expansion, Review


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Customises the django admin interface for the product model
    """
    list_display = [
        'name',
        'price',
        'pre_sale_price',
        'category',
        'card_set',
        'expansion',
        'date_added',
        'rating',
        'on_sale',
        'image'
    ]
    list_filter = ['category', 'card_set', 'expansion', 'on_sale']
    search_fields = ['name', 'description']

    summernote_fields = ('description',)

    actions = ['mark_on_sale', 'mark_not_on_sale']

    def mark_on_sale(self, request, queryset):
        """Marks product as on sale"""
        queryset.update(on_sale=1)
        self.message_user(
            request,
            'selected products have been marked on sale.'
        )

    def mark_not_on_sale(self, request, queryset):
        """Marks product as not on sale"""
        queryset.update(on_sale=0)
        self.message_user(
            request,
            'selected products have been marked not on sale.'
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the category model
    """
    list_display = ['display_name', 'name']


@admin.register(CardSet)
class CardSetAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the cardSet model
    """
    list_display = ['display_name', 'name']


@admin.register(Expansion)
class ExpansionAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the expansion model
    """
    list_display = ['display_name', 'name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the review model
    """
    list_display = [
        'user',
        'product',
        'review_rating',
        'review_text',
        'created_on',
        'approved'
    ]

    actions = ['reject', 'approve']

    def reject(self, request, queryset):
        """Marks a review as rejected"""
        queryset.update(approved=False)
        self.message_user(request, "Selected reviews have been rejected.")

    def approve(self, request, queryset):
        """Marks a review as approved"""
        queryset.update(approved=True)
        self.message_user(request, "Selected reviews have been approved.")
