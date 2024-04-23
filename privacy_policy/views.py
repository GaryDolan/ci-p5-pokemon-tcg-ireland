from django.shortcuts import render


def privacy_policy(request):
    """A function based view for displaying the Privacy policy ."""
    return render(request, 'privacy_policy.html')
