from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Contact

class ContactForm(forms.ModelForm):

    message = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Contact
        exclude = ['replied', 'resolved']

        widgets = {
            'name': forms.TextInput(attrs={'required': True, 'pattern': '^[a-zA-Z\\s]+$'}),
        }
        help_texts = {
            'name': 'Only letters and spaces allowed.',
        }