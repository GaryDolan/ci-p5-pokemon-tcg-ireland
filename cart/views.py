from django.shortcuts import render
from products.models import Product

def cart_view(request):
    """A function based view for displaying the home page."""


    return render(request, 'cart.html')
