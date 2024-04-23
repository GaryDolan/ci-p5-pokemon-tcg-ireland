"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('privacy_policy/', include('privacy_policy.urls')),
    path('about_us/', include('about_us.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'main.views.handler400'
handler401 = 'main.views.handler401'
handler403 = 'main.views.handler403'
handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
handler503 = 'main.views.handler503'
