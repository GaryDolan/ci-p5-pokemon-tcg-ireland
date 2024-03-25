from django.shortcuts import render
from .models import Product

def all_products(request):
    """A function based view for displaying all products, including sorts and searches."""

    products = Product.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'products.html', context)