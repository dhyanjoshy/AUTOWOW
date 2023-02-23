from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Dealerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','id':'username','name':'username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'password','name':'password'}),
        }