from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'shipping_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'shipping_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'shipping_cost',
                    'grand_total',)

    ordering = ('-date',)
# dont need to register the OrderLineItemAdmin class as its accessible via order admin model
admin.site.register(Order, OrderAdmin)