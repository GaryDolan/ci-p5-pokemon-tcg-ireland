from django.shortcuts import render


def about_us(request):
    """A function based view for displaying the About Us Page."""
    return render(request, 'about_us.html')
