from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """A function based view for displaying all products, including sorts and searches."""

    products = Product.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'products.html', context)

def product_detail(request, product_id):
    """A function based view for displaying a products full details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product':product,
    }

    return render(request, 'product_detail.html', context)