from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

def all_products(request):
    """A function based view for displaying all products, including sorts and searches."""

    products = Product.objects.all()

    # Will still be returned in context even if no value set below so needs a default value
    query = None
    categories = None
    on_sale = None
    sort = None
    direction = None

    if request.GET:
        # Sorting
        if 'sort' in request.GET:
            # Assign the value of the sort key to both
            sort_value = request.GET['sort']
            sort = sort_value

            # If sorting name add a new field to each product called lower_name (name in lower case)
            # Removes any uppercase so order_by method works correctly
            if sort_value == 'name':
                products = products.annotate(lower_name=Lower('name'))
                # we can then sort by lower name rather than name
                sort_value = 'lower_name'
                
            elif sort_value == 'category':
                # Double underscore allows access to related model fields
                products = products.annotate(lower_category_name=Lower('category__name'))
                sort_value = 'lower_category_name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_value = f'-{sort_value}'

            products = products.order_by(sort_value)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products':products,
        'search_term': query,
        'current_categories': categories,
        'on_sale': on_sale,
        'current_sorting': current_sorting,
    }

    return render(request, 'products.html', context)

def product_detail(request, product_id):
    """A function based view for displaying a products full details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product':product,
    }

    return render(request, 'product_detail.html', context)