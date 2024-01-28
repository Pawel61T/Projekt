from django import forms
from .models import Offer
from django.core import validators

class AddOffertForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ["user"]

class DisaplyUserOfferts(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['offer_type', 'price', 'size', 'capacity', 'number_of_rooms', 'address1']

class EditOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ["user"]