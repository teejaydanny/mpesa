from django import forms
from .models import RegistrationForm

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='enter your first name')
    last_name = forms.CharField(label='enter your last name')
    email = forms.EmailField(label='enter your email')
    password = forms.CharField(widget=forms.PasswordInput, label='enter your password')