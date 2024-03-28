from django.shortcuts import render
from products.models import Product

def index(request):
    """A function based view for displaying the home page."""

    new_products = Product.objects.order_by('-date_added')[:4]
    popular_products = Product.objects.order_by('-rating')[:4]

    context = {
        'new_products': new_products,
        'popular_products': popular_products,
    }

    return render(request, 'index.html', context)
