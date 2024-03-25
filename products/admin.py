from django.contrib import admin
from .models import Product, Category, CardSet, Expansion

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CardSet)
admin.site.register(Expansion)
