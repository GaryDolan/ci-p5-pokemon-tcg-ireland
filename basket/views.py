from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_basket(request):
    """A function based view for displaying the home page."""


    return render(request, 'basket.html')

def add_to_basket(request, item_id):
    
    # Get products for messaging
    product = get_object_or_404 (Product, pk=item_id)
    quantity = int (request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') 

    # use request response cycle session to store basket contents
    # if no basket create empty dict as basket, accessible site wide
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):

    # Get products for messaging
    product = get_object_or_404 (Product, pk=item_id)

    quantity = int (request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):

    # Get products for messaging
    product = get_object_or_404 (Product, pk=item_id)

    basket = request.session.get('basket', {})

    basket.pop(item_id)
    messages.success(request, f'Removed {product.name} from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
