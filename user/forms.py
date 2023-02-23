from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','id':'email','name':'email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','id':'firstname','name':'firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','id':'lastname','name':'lastname'}),          
            'password1':forms.PasswordInput(attrs={'class':'form-control','id':'password1','name':'password1'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','id':'password2','name':'password2'}),
        }

class Dealerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','id':'username','name':'username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','id':'password','name':'password'}),
        }