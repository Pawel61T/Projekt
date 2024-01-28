from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django.core import validators

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'description')

class SigninForm(forms.Form):
    email = forms.EmailField(max_length=65, required=True, error_messages = { 'required':"Please Enter your email."})
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, 
                               error_messages = { 'required':"Please Enter your password."})
    
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'description')