from django.shortcuts import render

def index(request):
    """A function based view for displaying the home page."""

    return render(request, 'index.html')