"""
Forms for handling contacts in the contact_us app.
"""
from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form for user to submit a contact request"""
    message = forms.CharField(widget=SummernoteWidget())

    class Meta:
        """
        Meta class to define form
        """
        model = Contact
        exclude = ['replied', 'resolved']

        widgets = {
            'name': forms.TextInput(
                attrs={'required': True, 'pattern': '^[a-zA-Z\\s]+$'}
            )
        }
        help_texts = {
            'name': 'Only letters and spaces allowed.'
        }
