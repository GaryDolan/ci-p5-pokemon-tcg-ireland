"""
Models for profiles app
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Model to represent a user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    default_country = CountryField(
        blank_label='Select country',
        null=True,
        blank=True
    )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
# pylint: disable=unused-argument
def create_or_update_profile(instance, created, **kwargs):
    """
    Uses the post_save signal of the user model to create a user
    profile related to the user, when a user is created
    """
    if created:
        # pylint: disable=no-member
        UserProfile.objects.create(user=instance)
    # not a newly created profile
    instance.userprofile.save()
