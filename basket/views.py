"""
Views for the basket app.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """A function based view for displaying the home page."""

    return render(request, 'basket.html')


def add_to_basket(request, item_id):
    """
    View to handel adding item to basket
    """
    # Get products for messaging
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # use request response cycle session to store basket contents
    # if no basket create empty dict as basket, accessible site wide
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        if basket[item_id] + quantity >= 99:
            original_qty = basket[item_id]
            quantity_to_add = 99 - basket[item_id]
            basket[item_id] += quantity_to_add
            messages.success(
                request,
                f'{original_qty} {product.name} already in your basket we '
                f'added {quantity_to_add} making your total the max of '
                f'{basket[item_id]}.'
            )
        else:
            basket[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {basket[item_id]}'
            )
    else:
        # Add a key, val pair to the basket dict
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    View to handel updating qty of product in basket
    """
    # Get products for messaging
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {basket[item_id]}'
        )
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    View to remove product from basket
    """
    # Get products for messaging
    product = get_object_or_404(Product, pk=item_id)

    basket = request.session.get('basket', {})

    basket.pop(item_id)
    messages.success(request, f'Removed {product.name} from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
