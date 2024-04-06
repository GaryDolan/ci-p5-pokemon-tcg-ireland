from django import forms

from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form for updating user profile"""

    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        