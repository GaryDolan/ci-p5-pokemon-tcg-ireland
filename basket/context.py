from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# Context processor, adds data to every template
# Basket details now available everywhere without returning it from view
def basket_contents(request):

    basket_items = []
    items_total = 0
    product_count = 0
    # Added to session in view
    basket = request.session.get('basket', {})

    #iterate through the session bag and populate context variables

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        items_total += quantity * product.price
        product_count += quantity
        
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })


    if items_total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = settings.STANDARD_SHIPPING_COST
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - items_total
    else:
        shipping = 0
        free_shipping_delta = 0
        
    basket_total = items_total +shipping

    context = {
        'basket_items': basket_items,
        'items_total': items_total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'basket_total': basket_total,
    }

    return context
