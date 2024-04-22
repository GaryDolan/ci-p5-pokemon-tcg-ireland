from django.shortcuts import render


def handler400(request, exception):
    """ Error Handler 400 - Bad Request """
    return render(request, "400.html", status=400)

def handler401(request, exception):
    """ Error Handler 401 - Unauthorized """
    return render(request, "401.html", status=401)

def handler403(request, exception):
    """ Error Handler 403 - Forbidden """
    return render(request, "403.html", status=403)

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)

def handler500(request):
    """ Error Handler 500 - Internal server Error """
    return render(request, "500.html", status=500)

def handler503(request, exception):
    """ Error Handler 503 - Service unavailable """
    return render(request, "503.html", status=503)