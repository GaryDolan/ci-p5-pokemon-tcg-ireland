from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from .models import Contact
from .forms import ContactForm


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message received, We will aim to contact you in the next 2 working days')
            return redirect(reverse('home'))
    else:
        # Declare dictionary to hold initial values
        initial = {}
        # Add any details we already have for a logged in user
        if request.user.is_authenticated:
            # set up the name  and email key value pairs
            initial['name'] = (
                f"{request.user.first_name} {request.user.last_name}")
            initial['email'] = request.user.email
        
        form = ContactForm(initial=initial)

    template = 'contact_us.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
