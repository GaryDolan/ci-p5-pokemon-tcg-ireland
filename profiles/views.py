from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        if 'edit_info' in request.POST:
            # Create a new instance of the UserProfileform using the post data
            # Update the instance of the profile we retrieved above
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')

    # Populate the form with current user information
    form = UserProfileForm(instance=profile)
    # Get all user orders
    orders = profile.orders.all()

    template = 'profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)