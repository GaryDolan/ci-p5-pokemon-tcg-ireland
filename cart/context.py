from django.conf import settings

# Context processor, adds data to every template
# Cart details now available everywhere without returning it from view
def cart_contents(request):

    cart_items = []
    items_total = 0
    product_count = 0

    if items_total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = settings.STANDARD_SHIPPING_COST
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - items_total
    else:
        shipping = 0
        free_shipping_delta = 0
        
    cart_total = items_total +shipping

    context = {
        'cart_items': cart_items,
        'items_total': items_total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'cart_total': cart_total,
    }

    return context
