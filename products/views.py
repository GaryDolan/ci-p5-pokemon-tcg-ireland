from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    """A function based view for displaying all products, including sorts and searches."""

    products = Product.objects.all()
    query = None
    categories = None
    on_sale = None

    if request.GET:
        # Filter by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            # Capture catagories objects in category list so we can access their fields in the template
            categories = Category.objects.filter(name__in=categories)
        
        # Filter by items on sale
        if 'on_sale' in request.GET:
            products = Product.objects.filter(on_sale=True)
            # check if 1 in template and if so display SALE in place of category name
            on_sale = 1

        # Search in name or description
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
        'current_categories': categories,
        'on_sale': on_sale,
    }

    return render(request, 'products.html', context)

def product_detail(request, product_id):
    """A function based view for displaying a products full details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product':product,
    }

    return render(request, 'product_detail.html', context)