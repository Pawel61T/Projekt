from django import forms
from .models import Offer, Reservation
from django.core import validators
from django.utils import timezone

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

class MakeReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'arrival_hour']
        widgets = {
            'check_in': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'check_out': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'arrival_hour': forms.TimeInput(attrs={'type': 'time'}  ),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        arrival_hour = cleaned_data.get('arrival_hour')
        time = timezone.now().time()
        if check_in and check_out:
            if check_in < timezone.now().date() or check_out < timezone.now().date():
                raise forms.ValidationError("Dates can not be set to day before todey.")
            if check_in > check_out:
                raise forms.ValidationError("Check in date can not be greater than Check out date.")
            if check_in == timezone.now().date() and check_out == timezone.now().date():
                if arrival_hour.hour <= time.hour or arrival_hour.minute <= time.minute:
                    raise forms.ValidationError('Please pick later hour.')
        return cleaned_data