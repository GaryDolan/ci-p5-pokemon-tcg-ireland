from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm, UserAccountForm

from checkout.models import Order
from wishlist.models import Wishlist

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Vars to track which form failed
    acc_form_failed = False
    profile_form_failed = False
    password_form_failed = False

    if request.method == 'POST':
        if 'edit_acc_info' in request.POST:
            user_account_form = UserAccountForm(request.POST, instance=request.user)
            if user_account_form.is_valid():
                user_account_form.save()
                messages.success(request, 'Account info updated successfully')
            else:
                messages.error(request, 'An error occurred updating your info, please try again')
                acc_form_failed = True
        elif 'edit_info' in request.POST:
            # Create a new instance of the UserProfileform using the post data
            # Update the instance of the profile we retrieved above
            user_profile_form = UserProfileForm(request.POST, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
                messages.success(request, 'Shipping info updated successfully')
            else:
                messages.error(request, 'An error occurred updating your shipping info, please try again')
                profile_form_failed = True
        elif 'edit_password' in request.POST:
            # Password change form uses user not instanc as parameter
            user_password_form = PasswordChangeForm(request.user, request.POST)
            if user_password_form.is_valid():
                user_password_form.save()
                messages.success(request, 'Password updated successfully')
            else:
                messages.error(request, 'An error occurred updating your password, please try again')
                password_form_failed = True
        
        # Render the template only initialising forms that have not failed validation.
        # If we failed a form submission return the same instance of the form to display error in validation.
        user_account_form = UserAccountForm(instance=request.user) if not acc_form_failed else user_account_form
        user_profile_form = UserProfileForm(instance=profile) if not profile_form_failed else user_profile_form
        user_password_form = PasswordChangeForm(request.user) if not password_form_failed else user_password_form

        # Get all user orders
        orders = profile.orders.all()

        template = 'profile.html'
        context = {
            'user_account_form': user_account_form,
            'user_profile_form': user_profile_form,
            'user_password_form': user_password_form,
            'orders': orders,
            'on_profile_page': True,
            'acc_form_failed': acc_form_failed,
            'profile_form_failed': profile_form_failed,
            'password_form_failed': password_form_failed,
        }

        return render(request, template, context) 
                
    else:
        # GET request so just display the page
        # Populate the forms with current user information
        user_account_form = UserAccountForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=profile)
        user_password_form = PasswordChangeForm(request.user)

        # Get all user orders
        orders = profile.orders.all()

        # Get user wishlist using related name
        # Get all products in user profiles wishlist
        user_wishlist = profile.user_wishlist
        wishlist_products = user_wishlist.products.all()

        template = 'profile.html'
        context = {
            'user_account_form': user_account_form,
            'user_profile_form': user_profile_form,
            'user_password_form': user_password_form,
            'orders': orders,
            'on_profile_page': True,
            'acc_form_failed': acc_form_failed,
            'profile_form_failed': profile_form_failed,
            'password_form_failed': password_form_failed,
            'wishlist_products': wishlist_products ,
        }

        return render(request, template, context)

@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
