from django.contrib import admin
from .models import Product, Category, CardSet, Expansion
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    list_display = ['name', 'price','category', 'card_set', 'expansion', 'date_added', 'rating', 'on_sale', 'image']
    list_filter = ['category', 'card_set', 'expansion', 'on_sale']
    search_fields = ['name', 'description']

    summernote_fields = ('description',)

    actions = ['mark_on_sale', 'mark_not_on_sale']	

    def mark_on_sale(self, request, queryset):
        queryset.update(on_sale=1)
        self.message_user(request, 'selected products have been marked on sale.')

    def mark_not_on_sale(self, request, queryset):
        queryset.update(on_sale=0)
        self.message_user(request, 'selected products have been marked not on sale.')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name']

@admin.register(CardSet)
class CardSetAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name']

@admin.register(Expansion)
class ExpansionAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name']    

