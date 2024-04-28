from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for checkout to collect user info.
    """

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)
        
        widgets = {
            'full_name': forms.TextInput(attrs={'required': True, 'pattern': '^[a-zA-Z\\s]+$'}),
            'phone_number': forms.TextInput(attrs={'required': True, 'pattern': '^(\d{10,})$'}),
        }
