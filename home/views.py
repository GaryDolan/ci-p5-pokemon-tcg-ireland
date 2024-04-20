from django.shortcuts import render
from django.db.models import Avg
from products.models import Product, Review


def index(request):
    """A function based view for displaying the home page."""

    new_products = Product.objects.order_by('-date_added')[:4]

    # Use reverse relationship to get products with approved reviews
    # distinct means only get each product once (may have multi reviews)
    reviewed_products = Product.objects.filter(review__isnull=False, review__approved=True).distinct()

    # Add a avg_rating field (annotate) to each product using the function to cal avg rating
    reviewed_products_with_rating = reviewed_products.annotate(avg_rating=Avg('review__review_rating'))

    #Order the products based on new avg rating field 
    popular_products = reviewed_products_with_rating.order_by('-avg_rating')[:4]

    context = {
        'new_products': new_products,
        'popular_products': popular_products,
    }

    return render(request, 'index.html', context)
