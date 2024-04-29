"""
Admin configurations for the checkout app
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Customises the django admin interface for the OrderLineItem model
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Customises the django admin interface for the Order model
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'shipping_cost',
              'order_total', 'grand_total', 'original_basket',
              'stripe_pid',)

    list_display = ('order_number', 'user_profile', 'date', 'full_name',
                    'order_total', 'shipping_cost',
                    'grand_total',)

    ordering = ('-date',)


# dont need to register the OrderLineItemAdmin class
# as its accessible via order admin model
admin.site.register(Order, OrderAdmin)
