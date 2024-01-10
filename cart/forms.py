from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOIICES = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField( choices=PRODUCT_QUANTITY_CHOIICES, label=_('Quantity'),coerce=int )
    override = forms.BooleanField( required=False, initial=False, widget=forms.HiddenInput )