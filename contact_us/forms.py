from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Contact

class ContactForm(forms.ModelForm):

    message = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Contact
        exclude = ['replied', 'resolved']