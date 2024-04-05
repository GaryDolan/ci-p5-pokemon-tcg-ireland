from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for checkout to collect user info.
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)