"""
Forms for handling profiles in the profiles app.
"""
from django import forms

from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form for updating user profile"""

    class Meta:
        """
        Meta class to define form
        """
        model = UserProfile
        exclude = ('user',)

        widgets = {
            'default_phone_number': forms.TextInput(attrs={
                'pattern': '^(\\d{10,})$'
                }),
            'default_town_or_city': forms.TextInput(attrs={
                'pattern': '^[a-zA-Z\\s]+$'
                }),
            'default_county': forms.TextInput(attrs={
                'pattern': '^[a-zA-Z\\s]+$'
                })
        }
        help_texts = {
            'default_phone_number': ('Enter a phone number with at least '
                                     '10 digits.'),
            'default_town_or_city': ('Only letters and spaces allowed.'),
            'default_county': ('Only letters and spaces allowed.')
        }


class UserAccountForm(forms.ModelForm):
    """Form for updating user first and last name"""
    class Meta:
        """
        Meta class to define form
        """
        model = User
        fields = ('first_name', 'last_name',)

        widgets = {
            'first_name': forms.TextInput(attrs={
                'required': True,
                'pattern': '^[a-zA-Z\\s]+$'
            }),
            'last_name': forms.TextInput(attrs={
                'required': True,
                'pattern': '^[a-zA-Z\\s]+$'
            })
        }
        help_texts = {
            'first_name': 'Only letters and spaces allowed.',
            'last_name': 'Only letters and spaces allowed.'
        }
