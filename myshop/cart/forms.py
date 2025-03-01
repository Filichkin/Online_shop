from django import forms
from django.utils.translation import gettext_lazy as _


PRODUCT_COUNT_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    count = forms.TypedChoiceField(
        choices=PRODUCT_COUNT_CHOICES,
        coerce=int,
        label=_('Количество')
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
