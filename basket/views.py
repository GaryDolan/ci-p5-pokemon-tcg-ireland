from django.shortcuts import render, redirect

def basket_view(request):
    """A function based view for displaying the home page."""


    return render(request, 'basket.html')

def add_to_basket(request, item_id):

    quantity = int (request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') 

    # use request response cycle session to store basket contents
    # if no basket create empty dict as basket, accessible site wide
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
