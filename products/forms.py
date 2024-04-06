from django import forms

from django.contrib.auth.models import User

from .models import Product, Category, CardSet, Expansion


class ProductForm(forms.ModelForm):
    """ Form for updating products"""

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        card_sets = CardSet.objects.all()
        expansions = Expansion.objects.all()
        # For each category create a tuple with its id and display name
        category_display_names = [(c.id, c.get_display_name()) for c in categories]
        card_set_display_names= [(cs.id, cs.get_display_name()) for cs in card_sets]
        expansion_display_names = [(e.id, c.get_display_name()) for e in expansions]
        
        self.fields['category'].choices = category_display_names
        self.fields['card_set'].choices = card_set_display_names
        self.fields['expansion'].choices = expansion_display_names
