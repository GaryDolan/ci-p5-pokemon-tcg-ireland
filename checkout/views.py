from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from basket.context import basket_contents

import stripe
import json

# Post request made to this view before stripe confirm card payment method
# Post request will contain client secret from the payment intent
@require_POST
def cache_checkout_data(request):
    try:
        # Split the client secret to get the payment intent id (pid)
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set up strip with key so we can modify the payment intent before submission to stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify the metadata to include user, save info choice and basket
        # This means when a webhook is returned from stripe we have access
        # to all this data in the webhook, and can ensure if payment is successful we create the order instance.
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
    
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Handel form submission, create instance of the order with line items
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        # Put the posted form data into dict 
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Create instance of form using submitted data
        order_form = OrderForm(form_data)

        # if form valid save the order and create line items
        if order_form.is_valid():
            order = order_form.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                            Please double check your information.')

    # Request is a GET
    else:
        # Return to products if basket empty
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your basket is empty")
            return redirect(reverse('products'))

        # Use basket context function to retrieve basket total for stripe
        current_basket = basket_contents(request)
        total = current_basket['basket_total']
        # Stripe needs an int
        stripe_total = round (total *100)
        # Set secret key on stripe
        stripe.api_key = stripe_secret_key
        # Create payment intent 
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # Did the user tick save details on form
    save_info = request.session.get('save_info')
    # get order details of order that just succeeded and called this view
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
