from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from profiles.models import UserProfile
from products.models import Product




class Wishlist(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                      related_name='user_wishlist')
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user_profile.user.username}'s wishlist"


