"""
Views for the wishlist app.
"""
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist


@login_required
def wishlist_toggle(request, product_id):
    """
    View to toggle a product in or out of wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = request.user.userprofile

    wishlist_item_exists = Wishlist.objects.filter(
        user_profile=user_profile, products=product
    ).exists()

    # Add or remove the product from wishlist base on if it exists
    if wishlist_item_exists:
        wishlist_item = Wishlist.objects.get(
            user_profile=user_profile, products=product
        )
        wishlist_item.products.remove(product)
        messages.success(
            request, f'{product.name} has been removed from your wishlist'
        )
    else:
        wishlist = Wishlist.objects.get(
            user_profile=user_profile
        )
        wishlist.products.add(product)
        wishlist.save()
        messages.success(
            request, f'{product.name} has been added to your wishlist'
        )

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def wishlist_remove(request, product_id):
    """
    View to handle removing product from wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = request.user.userprofile

    wishlist_item = Wishlist.objects.get(
        user_profile=user_profile, products=product
    )
    wishlist_item.products.remove(product)
    messages.success(
        request, f'{product.name} has been removed from your wishlist'
    )

    return redirect(reverse('profile'))
