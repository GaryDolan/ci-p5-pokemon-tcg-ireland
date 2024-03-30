from django.shortcuts import render, redirect

def cart_view(request):
    """A function based view for displaying the home page."""


    return render(request, 'cart.html')

def add_to_cart(request, item_id):

    quantity = int (request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url') 

    # use request response cycle session to store cart contents
    # if no cart create empty dict as cart
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
