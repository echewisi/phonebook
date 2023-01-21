from django import forms
from .models import Individual, Contact
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User= get_user_model

class IndividualForm(UserCreationForm):
    class meta:
        model= User
        fields=  ['username', 'firstname', 'lastname', 'email', 'password', 'contacts']

class ContactForm(forms.ModelForm):
    class meta:
        model= Contact
        fields=['name', 'number', 'email', 'sitelinks', 'date_of_birth']
