from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def all_products(request):
    """A function based view for displaying all products, including sorts and searches."""

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search text")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products':products,
        'search_term': query,
    }

    return render(request, 'products.html', context)

def product_detail(request, product_id):
    """A function based view for displaying a products full details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product':product,
    }

    return render(request, 'product_detail.html', context)