from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from wishlist.models import Wishlist

from .models import Product, Category
from .forms import ProductForm


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
        # SORTING
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

        # FILTERING
        # By category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            # Capture catagories objects in category list so we can access their fields in the template
            categories = Category.objects.filter(name__in=categories)
        
        # By card set
        if 'card_set' in request.GET:
            card_set_name = request.GET['card_set']
            products = products.filter(card_set__name=card_set_name)
        
        # By expansion
        if 'expansion' in request.GET:
            expansion_name = request.GET['expansion']
            products = products.filter(expansion__name=expansion_name)


        # By items on sale
        if 'on_sale' in request.GET:
            products = products.filter(on_sale=True)
            # check if 1 in template and if so display SALE in place of category name
            on_sale = 1

        # SEARCH (in name or description)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search text")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'on_sale': on_sale,
        'current_sorting': current_sorting,
    }

    return render(request, 'products.html', context)

def product_detail(request, product_id):
    """A function based view for displaying a products full details"""

    product = get_object_or_404(Product, pk=product_id)
    product_in_wishlist = False

    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        product_in_wishlist = Wishlist.objects.filter(user_profile=user_profile, products=product).exists()

    context = {
        'product': product,
        'product_in_wishlist': product_in_wishlist, 
    }

    return render(request, 'product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Set product here so we can redirect to it after creation
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    
    template = 'add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # Create a form using post request data and files and same from products
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
